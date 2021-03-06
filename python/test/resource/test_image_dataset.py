from vmaf.config import VmafConfig

dataset_name = 'test_image'
yuv_fmt = 'yuv444p'

ref_videos = [
 {'content_id': 0,
  'content_name': '100007',
  'height': 321,
  'path': VmafConfig.test_resource_path('test_image_yuv', '100007.yuv'),
  'width': 481},
 {'content_id': 1,
  'content_name': '100039',
  'height': 321,
  'path': VmafConfig.test_resource_path('test_image_yuv', '100039.yuv'),
  'width': 481},
 {'content_id': 2,
  'content_name': '100075',
  'height': 321,
  'path': VmafConfig.test_resource_path('test_image_yuv', '100075.yuv'),
  'width': 481},
 {'content_id': 4,
  'content_name': '100098',
  'height': 321,
  'path': VmafConfig.test_resource_path('test_image_yuv', '100098.yuv'),
  'width': 481},
 {'content_id': 5,
  'content_name': '100099',
  'height': 321,
  'path': VmafConfig.test_resource_path('test_image_yuv', '100099.yuv'),
  'width': 481},
 {'content_id': 6,
  'content_name': '10081',
  'height': 321,
  'path': VmafConfig.test_resource_path('test_image_yuv', '10081.yuv'),
  'width': 481},
 {'content_id': 7,
  'content_name': '101027',
  'height': 321,
  'path': VmafConfig.test_resource_path('test_image_yuv', '101027.yuv'),
  'width': 481},
 {'content_id': 12,
  'content_name': '102062',
  'height': 321,
  'path': VmafConfig.test_resource_path('test_image_yuv', '102062.yuv'),
  'width': 481},
]

dis_videos = [
 {'asset_id': 0,
  'content_id': 0,
  'path': VmafConfig.test_resource_path('test_image_yuv', '100007.yuv'), 'mos': 2.5},
 {'asset_id': 1,
  'content_id': 1,
  'path': VmafConfig.test_resource_path('test_image_yuv', '100039.yuv'), 'mos': 3.9},
 {'asset_id': 2,
  'content_id': 2,
  'path': VmafConfig.test_resource_path('test_image_yuv', '100075.yuv'), 'mos': 5.0},
 {'asset_id': 4,
  'content_id': 4,
  'path': VmafConfig.test_resource_path('test_image_yuv', '100098.yuv'), 'mos': 4.2},
 {'asset_id': 5,
  'content_id': 5,
  'path': VmafConfig.test_resource_path('test_image_yuv', '100099.yuv'), 'mos': 4.1},
 {'asset_id': 6,
  'content_id': 6,
  'path': VmafConfig.test_resource_path('test_image_yuv', '10081.yuv'), 'mos': 4.6},
 {'asset_id': 7,
  'content_id': 7,
  'path': VmafConfig.test_resource_path('test_image_yuv', '101027.yuv'), 'mos': 4.9},
 {'asset_id': 12,
  'content_id': 12,
  'path': VmafConfig.test_resource_path('test_image_yuv', '102062.yuv'), 'mos': 3.3},
]
