#/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2011-2013, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from py2neo import neo4j, node


def test_can_remove_labels_from_node():
    graph_db = neo4j.GraphDatabaseService()
    alice, = graph_db.create(node(name="Alice"))
    alice.labels.add("human", "female")
    labels = alice.labels
    assert len(labels) == 2
    assert labels == {"human", "female"}
    alice.labels.remove("human")
    labels = alice.labels
    assert labels == {"female"}
    assert labels != {"human", "female"}
    alice.labels.remove("female")
    labels = alice.labels
    assert labels == set()