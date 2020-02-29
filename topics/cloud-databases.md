## Cloud Databases

A big takaway in the cloud is you don't have to start with a relational database.  The CTO of Amazon, Werner Vogel's brings up some of the options available in the blog post [A one size fits all database doesn't fit anyone](https://www.allthingsdistributed.com/2018/06/purpose-built-databases-in-aws.html). 

![all things distributed](https://www.allthingsdistributed.com/images/databases.png) *source: allthingsdistributed.com*

## Key Value Databases

A good example of a serverless key/value database is [Dynamodb](https://aws.amazon.com/dynamodb/).

![alt text](https://d1.awsstatic.com/video-thumbs/dynamodb/AWS-online-games-wide.ada4247744e9be9a6d857b2e13b7eb78b18bf3a5.png)

How could you query it in Python?

```python
def query_police_department_record_by_guid(guid):
    """Gets one record in the PD table by guid
    
    In [5]: rec = query_police_department_record_by_guid(
        "7e607b82-9e18-49dc-a9d7-e9628a9147ad"
        )
    
    In [7]: rec
    Out[7]: 
    {'PoliceDepartmentName': 'Hollister',
     'UpdateTime': 'Fri Mar  2 12:43:43 2018',
     'guid': '7e607b82-9e18-49dc-a9d7-e9628a9147ad'}
    """
    
    db = dynamodb_resource()
    extra_msg = {"region_name": REGION, "aws_service": "dynamodb", 
        "police_department_table":POLICE_DEPARTMENTS_TABLE,
        "guid":guid}
    log.info(f"Get PD record by GUID", extra=extra_msg)
    pd_table = db.Table(POLICE_DEPARTMENTS_TABLE)
    response = pd_table.get_item(
        Key={
            'guid': guid
            }
    )
    return response['Item']
```

## Graph Databases

**Why Not Relational Databases?**
* Relationship data not good for relational databases.
* Example:
  * Think about SQL query of social network used to select all third-degree connections of individual.
    * Imagine number of joins needed.
* Think about SQL query used to get full social network of individual.
    * Imagine number of recursive joins required.
* Relational databases good at representing one-to-many relationships, in which one table connected to multiple tables.

### AWS Neptune

* [AWS Neptune](https://aws.amazon.com/neptune/)

![Neptune](https://user-images.githubusercontent.com/58792/61985896-8d9ab080-afd9-11e9-880c-57f9d8a1d953.png)

### Neo4j

* [Neo4j Website](https://neo4j.com/)
* [Neo4j Sandbox](https://neo4j.com/sandbox-v2/?ref=hcard)

#### Key Concepts

[reference Neo4j website sandbox tutorial ](https://neo4j.com/sandbox-v2/?ref=hcard#)

##### Graph Database

*Graph Database* can store: 

*  **Nodes** - graph data records
* **Relationships** - connect nodes
* **Properties** - named data values

##### Simplest Graph

*Simplest Graph*

* **One node**
* Has **some properties**

1. Start by drawing a circle for the node
2. Add the name Emil
3. Note that he is from Sweden

* Nodes are the name for data records in a graph
* Data is stored as Properties
* Properties are simple name/value pairs

![alt text](https://user-images.githubusercontent.com/58792/61905247-a67e6580-aef6-11e9-8f94-816f57915e1a.png)

##### Labels

Nodes can be grouped together by applying a Label to each member. In our social graph, we'll label each node that represents a Person.

1. Apply the label "Person" to the node we created for Emil
2.  Color "Person" nodes red
* A node can have zero or more labels
* Labels do not have any properties

![Nodes](https://user-images.githubusercontent.com/58792/61907644-df6d0900-aefb-11e9-9ef1-cc8b088813e1.png)

##### More Nodes

Like any database, storing data in Neo4j can be as simple as adding more records. We'll add a few more nodes:

1.  Emil has a klout score of 99
2.  Johan, from Sweden, who is learning to surf
3.  Ian, from England, who is an author
4.  Rik, from Belgium, has a cat named Orval
5.  Allison, from California, who surfs

* Similar nodes can have different properties
* **Properties** can be **strings**, **numbers**, or **booleans**
* Neo4j can **store billions of nodes**

![more_nodes](https://user-images.githubusercontent.com/58792/61908143-0d068200-aefd-11e9-9ad1-7187171b3fe2.png)

##### Relationships

The real power of Neo4j is in connected data. To associate any two nodes, add a Relationship which describes how the records are related.

In our social graph, we simply say who KNOWS whom:

1. Emil KNOWS Johan and Ian
2. Johan KNOWS Ian and Rik
3. Rik and Ian KNOWS Allison

* Relationships always have direction
* Relationships always have a type
* Relationships form patterns of data

![relationships](https://user-images.githubusercontent.com/58792/61908425-a5046b80-aefd-11e9-9a48-9ba19564e24d.png)

##### Relationship Properties

In a property graph, **relationships are data records** that can also** contain properties**. Looking more closely at Emil's relationships, note that:

* Emil **has known Johan since 2001**
* Emil **rates Ian 5 (out of 5)**
* Everyone else can have similar relationship properties

![relationships](https://user-images.githubusercontent.com/58792/61909193-78515380-aeff-11e9-95ff-59d7f8c1c30b.png)

#### Key Graph Algorithms (With neo4j)

* **Centrality** - What are the most important nodes in the network? *PageRank, Betweenness Centrality, Closeness Centrality*

* **Community detection** - How can the graph be partitioned? *Union Find, Louvain, Label Propagation, Connected Components*

* **Pathfinding** - What are the shortest paths or best routes available given cost? *Minimum Weight Spanning Tree, All Pairs- and Single Source- Shortest Path, Dijkstra*



```Cypher
CALL dbms.procedures()
YIELD name, signature, description
WITH * WHERE name STARTS WITH "algo"
RETURN *
```

#### Russian Troll Walkthrough [Demo]

To run through example run this cipher code in their sandbox

```Cypher
:play https://guides.neo4j.com/sandbox/twitter-trolls/index.html
```

##### Finding top Trolls with Neo4J

* [Russian Twitter account pretending to be Tennessee GOP fools celebrities, politicians](https://www.chicagotribune.com/business/blue-sky/ct-russian-twitter-account-tennessee-gop-20171018-story.html)

The list of prominent people who tweeted out links from the account, **@Ten_GOP**, which Twitter shut down in August, includes political figures such as **Michael Flynn** and **Roger Stone**, celebrities such as **Nicki Minaj** and **James Woods**, and media personalities such as **Anne Coulter** and **Chris Hayes**

A screenshot of the Neo4J interface for the phrase "thanks obama".
![Screen Shot 2020-02-29 at 4 06 34 PM](https://user-images.githubusercontent.com/58792/75615076-84446a00-5b0d-11ea-9ebc-8e4b56db64c5.png)



**Pagerank score for Trolls**

Here is a walkthrough of code in a colab notebook you can reference called [social network theory](https://github.com/noahgift/cloud-data-analysis-at-scale/blob/master/social_network_theory.ipynb).

```python
def enable_plotly_in_cell():
  import IPython
  from plotly.offline import init_notebook_mode
  display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
  '''))
  init_notebook_mode(connected=False)
```

The trolls are exported from Neo4j and they are imported in Pandas.

```python
import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/noahgift/essential_machine_learning/master/pagerank_top_trolls.csv")
df.head()
```

![Screen Shot 2020-02-29 at 4 02 33 PM](https://user-images.githubusercontent.com/58792/75615028-f8324280-5b0c-11ea-8319-ce0d459fd261.png)

Next up, the data is graphed with Plotly.

```python
import plotly.offline as py
import plotly.graph_objs as go

from plotly.offline import init_notebook_mode
enable_plotly_in_cell()
init_notebook_mode(connected=False)


fig = go.Figure(data=[go.Scatter(
    x=df.pagerank,
    text=df.troll,
    mode='markers',
    marker=dict(
        color=np.log(df.pagerank),
        size=df.pagerank*5),
)])
py.iplot(fig, filename='3d-scatter-colorscale')
```

![Screen Shot 2020-02-29 at 4 09 56 PM](https://user-images.githubusercontent.com/58792/75615120-f5841d00-5b0d-11ea-92c9-2c7fe22d303e.png)

**Top Troll Hashtags**

```python
import pandas as pd
import numpy as np

df2 = pd.read_csv("https://raw.githubusercontent.com/noahgift/essential_machine_learning/master/troll-hashtag.csv")
df2.columns = ["hashtag", "num"]
df2.head()
```

![Screen Shot 2020-02-29 at 4 11 42 PM](https://user-images.githubusercontent.com/58792/75615139-33814100-5b0e-11ea-9c59-81c75d9b82e3.png)

Now plot these troll hashtags.

```python
import plotly.offline as py
import plotly.graph_objs as go

from plotly.offline import init_notebook_mode
enable_plotly_in_cell()
init_notebook_mode(connected=False)


fig = go.Figure(data=[go.Scatter(
    x=df.pagerank,
    text=df2.hashtag,
    mode='markers',
    marker=dict(
        color=np.log(df2.num),
        size=df2.num),
)])
py.iplot(fig)
```

You can see these trolls love to use the hashtag #maga.

![Screen Shot 2020-02-29 at 4 14 47 PM](https://user-images.githubusercontent.com/58792/75615178-a4285d80-5b0e-11ea-9cfe-c089bd407990.png)


### References

*   [The Anatomy of a Large-Scale Hypertextual Web Search Engine](http://infolab.stanford.edu/~backrub/google.html)
*   [Graph Databases, 2nd Edition](https://learning.oreilly.com/library/view/graph-databases-2nd/9781491930885/)
*   [Neo4J](https://neo4j.com/blog/story-behind-russian-twitter-trolls/)
