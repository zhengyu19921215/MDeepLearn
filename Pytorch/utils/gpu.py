#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：gpu_computing
   Description :  Pytorch 使用 GPU计算的工具设置
   Email : autuanliu@163.com
   Date：2018/1/3
"""

import torch
import torch.nn as nn
from torch.autograd import Variable

# 类型定义
_data_type = torch.FloatTensor
_data_type1 = torch.LongTensor


def gpu(model, data, target):
    """使得模型和数据利用GPU资源

    如果存在多块GPU, 使得模型在GPU上获得并行运算支持,
    使得数据在GPU上进行计算

    Parameters
    ----------
    :param model: class instance
        model instance
    :param data: numpy array
        train or test data
    :param target: numpy array
        train or test target

    Returns
    -------
    :return model_new: class instance
        cuda transformed instance
    :return data_new: torch.autograd.Variable
        cuda transformed
    :return target_new: torch.autograd.Variable
        cuda transformed
    """
    # 初始化
    model_new = model

    if torch.cuda.is_available():
        # GPU, CPU, 并行等处理
        if torch.cuda.device_count() > 1:
            model_new = nn.DataParallel(model)
        else:
            model_new = model.cuda()

        # 必须重命名, 否则无效
        data_new = Variable(torch.from_numpy(data).cuda())
        target_new = Variable(torch.from_numpy(target).cuda())
    else:
        data_new = Variable(torch.from_numpy(data))
        # 某些损失函数需要 tensor.type(torch.LongTensor) 类型, 如 NLLLoss
        # 根据情况更改
        target_new = Variable(torch.from_numpy(target))

    return model_new, data_new, target_new


def gpu_t(model, data, target):
    """使得模型和数据利用GPU资源

    如果存在多块GPU, 使得模型在GPU上获得并行运算支持,
    使得数据在GPU上进行计算

    Parameters
    ----------
    :param model: class instance
        model instance
    :param data: tensor
        train or test data
    :param target: tensor
        train or test target

    Returns
    -------
    :return model_new: class instance
        cuda transformed instance
    :return data_new: torch.autograd.Variable
        cuda transformed
    :return target_new: torch.autograd.Variable
        cuda transformed
    """
    # 初始化
    model_new = model

    if torch.cuda.is_available():
        # GPU, CPU, 并行等处理
        if torch.cuda.device_count() > 1:
            model_new = nn.DataParallel(model)
        else:
            model_new = model.cuda()

        # 必须重命名, 否则无效
        data_new = Variable(data.cuda())
        # 某些损失函数需要 tensor.type(torch.LongTensor) 类型, 如 NLLLoss
        # 根据情况更改
        target_new = Variable(target.cuda())
    else:
        data_new = Variable(data)
        target_new = Variable(target)

    return model_new, data_new, target_new
