"""
开始训练文件，此次开始onestage pipeline将当前所有一阶段的目标检测工具
整合到这里。
"""
import argparse

from utils.utils import *

# Setup_Parser
def get_parser():
    parser = argparse.ArgumentParser(description='OneStage for All')
    parser.add_argument(
        '--cfg', type=str,
        default='models/yolov5s_wheat.yaml',
        help='model.yaml path'
    )
    parser.add_argument(
        '--data', type=str,
        default='data/wheat.yaml',
        help='data.yaml path'
    )
    parser.add_argument(
        '--hyp', type=str,
        default='',
        help='hyp.yaml path (optional)'
    )
    parser.add_argument(
        '--epochs', type=int,
        default=300
    )
    parser.add_argument(
        '--batch-size', type=int,
        default=2,
        help="Total batch size for all gpus"
    )
    parser.add_argument(
        '--resume', nargs='?', const='get_last',
        default=False,
        help='resume from given path/to/last.pt, or most recent run if blank.'
    )
    parser.add_argument(
        '--weights', type=str,
        default='',
        help='initial weights path'
    )

    return parser


def main():
    opt = get_parser().parse_args()

    last = get_latest_run() if opt.resume == 'get_last' else opt.resume
    if last and not opt.weights:
        print(f'Resuming training from {last}')
    opt.weights = last if opt.resume and not opt.weights else opt.weights
    print(1)




if __name__ == '__main__':
    main()
