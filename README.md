# ConceptVisualization

⌛This a project that build a Django-based web app that supports building relations among concepts.

☺️On the **main page**, users can add multiple concept graphs. By clicking on them, users can navigate to each concept graph for visualization.
  -  The graph title is accompanied by a number that represents the number of nodes in the graph.
  -  Whenever a user creates a new graph, the first node name is the same as the graph title and has the type of ``Title``.

☺️On the **graph page**, users can visualize the concept relations. 
  -  Each node has a border color that represents its type: ``Title``, ``Attribute``, ``Example``, ``Reason``, or ``Theory``.
  -  By clicking the ``+``, users can see the details of each node. They can also vote up or down to express their agreement or disagreement.
  -  Furthermore, users can add a new node to the current node.
  -  Users can also delete the current node. If this current node has any child, the child will also be deleted.
 
☺️ Error Handling
  - Users cannot create graph/node that is already existed or with empty title.

☺️ Upcoming functionalities
  -  Comments for each nodes.
  -  Real-time chatbox using channels provided by Django.
