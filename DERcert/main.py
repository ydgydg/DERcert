import copy
from random import choice
import GetCerts.get_cert
import MutateCerts.mutate
import MutateCerts.locate_oid
import ParseCerts.getfile
import ParseCerts.dump
import ParseCerts.draw
import SaveCerts.savetxt
import SaveCerts.hextoder
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import Config
from pycallgraph import GlobbingFilter


def main():

        GetCerts.get_cert.get_cert_batch('websites.txt', 443, '/home/ydg/test_pem')
        data = ParseCerts.getfile.get_filebindata('./test0.der')
        data1 = data
        # Parse

        result = ParseCerts.dump.dump(data)
        result_copy_1 = copy.deepcopy(result)

        edge = []
        node = []
        ParseCerts.draw.draw(data,result_copy_1, "cert tree")

        # mutate
        # change value
        result_copy_2 = copy.deepcopy(result)
        node_2 = []
        MutateCerts.mutate.solve_tree(result_copy_2, node_2, None)
        # Leaf nodes are selected at random
        node_change= choice(list(filter(lambda x: x["isNode"], node_2)))
        MutateCerts.mutate.change_value(node_2,node_change)

        # add
        result_copy_3 = copy.deepcopy(result)
        node_3 = []
        MutateCerts.mutate.solve_tree(result_copy_3, node_3, None)
        node_add = choice(list(filter(lambda x: x["isNode"], node_3)))
        MutateCerts.mutate.add(node_3,node_add, "11111111")
        ParseCerts.draw.draw(data,result_copy_3,'test')

        # delete
        result_copy_4 = copy.deepcopy(result)
        node_4 = []
        MutateCerts.mutate.solve_tree(result_copy_4, node_4, None)
        node_del = choice(list(filter(lambda x: x["isNode"], node_3)))
        MutateCerts.mutate.delete(node_4,node_del)


        # OID
        # Location oid and draw
        result_copy_5 = copy.deepcopy(result)
        node_5 = []
        MutateCerts.mutate.solve_tree(result_copy_5, node_5, None)
        filtered_nodes = list(filter(lambda x: x["isNode"], node_5))
        find_node, start, end = MutateCerts.locate_oid.find_oid_node(filtered_nodes, "551d0f")
        node_v = find_node.get("node-value", [])
        # intercept OID
        oid_data = node_v[start: end]
        OID_NODE_ID = find_node["node-id"]
        oid_node = []
        oid_edge = []
        oid_result = ParseCerts.dump.dump(oid_data)
        MutateCerts.locate_oid.parse_oid(None, oid_result)

        oid_result_copy_1 = copy.deepcopy(result)
        oid_node_1 = []
        MutateCerts.mutate.solve_tree(oid_result_copy_1, oid_node_1, None)
        curr_oid_node = list(filter(lambda x: x["node-id"] == OID_NODE_ID, oid_node_1))[0]
        # Prepare data -- OID tree structure
        oid_sub_result_copy_1 = copy.deepcopy(oid_result)
        oid_sub_node_1 = []
        MutateCerts.mutate.solve_tree(oid_sub_result_copy_1, oid_sub_node_1, None)

        random_oid_node = choice(list(filter(lambda x: x["isNode"], oid_sub_node_1)))
        MutateCerts.mutate.change_value(oid_sub_node_1,random_oid_node)

        trans_result = MutateCerts.mutate.result_to_binary(oid_sub_result_copy_1)
        curr_oid_node["node-value"] = curr_oid_node["node-value"][:start] + trans_result + curr_oid_node["node-value"][end:]
        final_binary = MutateCerts.mutate.result_to_binary(oid_node_1)

        SaveCerts.savetxt.result_to_file(data,'./txt/test.txt')

        SaveCerts.hextoder.save_der()



if __name__ == '__main__':
    config = Config()
    config.trace_filter = GlobbingFilter(include=[
        'main',
        'GetCerts.*',
        'MutateCerts.*',
        'ParseCerts.*',
        'SaveCerts.*'
    ])
    graphviz = GraphvizOutput()
    graphviz.output_file = './graph/call_graph.pdf'

    with PyCallGraph(output=graphviz, config=config):
        main()