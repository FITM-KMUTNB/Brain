from neo4j import GraphDatabase  # pip install neo4j

# Neo4j-Driver --> connect via bolt protocol
driver = GraphDatabase.driver(
    'bolt://localhost:7687', auth=('neo4j', 'tmrs_2019'))
session = driver.session()


def createNode(props):
    Label = 'SINGLE_NODE'
    return session.run("CREATE (a:"+Label+" {props}) "
                       "RETURN id(a)",  {'props': props}).single().value()


def createRelation(n1, n2, props):
    Label = 'SINGLE_NODE'
    return session.run("MATCH (a:"+Label+"),(b:"+Label+") WHERE a.name = {n1} AND b.name = {n2} "
                       "CREATE (a)-[rel:IS_CONNECTED {props}]->(b) RETURN rel",  {'n1': n1, 'n2': n2, 'props': props}).single().value()


createNode({'name': 'man', 'occur': 3})
createNode({'name': 'woman', 'occur': 4})
createNode({'name': 'year', 'occur': 1})
createNode({'name': 'baby', 'occur': 2})

createRelation('man', 'woman', {'count': 3, 'dice': 0.5})
createRelation('man', 'year', {'count': 1, 'dice': 0.5})
createRelation('man', 'baby', {'count': 1, 'dice': 0.5})
createRelation('year', 'woman', {'count': 1, 'dice': 0.5})
createRelation('woman', 'baby', {'count': 2, 'dice': 0.5})

driver.close()
