#!/usr/bin/python

import pandas as pd
from flask_app import db
from flask_app import Joint
from flask_app import Station
from flask_app import Category

class Populater:
    def populate_atrain(self):

        # import raw csv data
        joints = pd.read_csv('/home/ianwright/visualize/visualize-nyc/data/atrain/joints.csv', index_col=0)
        categories = pd.read_csv('/home/ianwright/visualize/visualize-nyc/data/atrain/categories.csv', index_col=0)
        stations = pd.read_csv('/home/ianwright/visualize/visualize-nyc/data/atrain/stations.csv', index_col=0)
        #joint_category_map = pd.read_csv('/home/ianwright/visualize/visualize-nyc/data/atrain/joint_category_map.csv', index_col=0)
        #station_joint_map = pd.read_csv('/home/ianwright/visualize/visualize-nyc/data/atrain/station_joint_map.csv', index_col=0)

        # load joints
        for ind, joint in joints.iterrows():
            joint_list = joint.tolist()
            db.session.merge(
                Joint(ind, *joint_list)
                )
            db.session.commit()

        # load categories
        for ind, cat in categories.iterrows():
            cat_list = cat.tolist()
            db.session.merge(
                Category(ind, *cat_list)
                )
            db.session.commit()

        # load stations
        for ind, station in stations.iterrows():
            station_list = station.tolist()
            db.session.merge(
                Station(ind, *station_list)
                )
            db.session.commit()


populater = Populater()
