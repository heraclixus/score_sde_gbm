# coding=utf-8
# Copyright 2020 The Google Research Authors.
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

# Lint as: python3
"""Training DDPM with VP SDE."""

from configs.default_cifar10_configs import get_default_configs

def get_config():
  config = get_default_configs()
  # training
  training = config.training
  training.sde = 'loggbm'
  training.continuous = True
  training.reduce_mean = True
  training.n_iters = 300000
  training.snapshot_freq = 20000
  training.log_freq = 500
  training.eval_freq = 500

  # sampling
  sampling = config.sampling
  sampling.method = 'pc'
  sampling.predictor = 'euler_maruyama'
  sampling.corrector = 'none'

  # data
  data = config.data
  data.centered = False

  # model
  model = config.model
  model.name = 'ddpm'
  model.scale_by_sigma = False
  model.ema_rate = 0.9999
  model.normalization = 'GroupNorm'
  model.nonlinearity = 'swish'
  model.nf = 128
  model.ch_mult = (1, 2, 2, 2)
  model.num_res_blocks = 2
  model.attn_resolutions = (16,)
  model.resamp_with_conv = True
  model.conditional = True
  model.num_scales = 500  # TODO: step N
  model.beta_min = 0.0
  model.beta_max = 30    # TODO: max beta value, could be smaller? 
 

  # optim
  optim = config.optim
  optim.lr = 1e-4
  optim.beta1 = 0.9

  return config
