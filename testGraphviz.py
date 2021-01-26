def test():
    test2()


def test2():
    test3()


def test3():
    print('test')

def main():
    test()

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import Config
from pycallgraph import GlobbingFilter

if __name__ == "__main__":
    config = Config()

    config.trace_filter = GlobbingFilter(include=[
        'main',
        'draw_chessboard',
        'draw_chessman',
        'draw_chessboard_with_chessman',
        'choose_save',
        'choose_turn',
        'choose_mode',
        'choose_button',
        'save_chess',
        'load_chess',
        'play_chess',
        'pop_window',
        'tip',
        'get_score',
        'max_score',
        'win',
        'key_control'
    ])

    graphviz = GraphvizOutput()
    graphviz.output_file = 'D:\\dev-tool-for-python\\graph.png'
    with PyCallGraph(output=graphviz, config=config):
        main()