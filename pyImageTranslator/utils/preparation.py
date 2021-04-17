from pyImageTranslator.utils.entity import FakeArgs

__work__ = False

fakeArgs = FakeArgs()
# 可换参数
setattr(
    fakeArgs, "cls_model_dir",
    "D:\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\interence\\ch_ppocr_mobile_v2.0_cls_infer\\"
) if not __work__ else setattr(
    fakeArgs, "cls_model_dir",
    "D:\\github_repo\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\interence\\ch_ppocr_mobile_v2.0_cls_infer\\"
)
setattr(
    fakeArgs, "det_model_dir",
    "D:\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\interence\\ch_ppocr_server_v2.0_det_infer\\"
) if not __work__ else setattr(
    fakeArgs, "det_model_dir",
    "D:\\github_repo\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\interence\\ch_ppocr_server_v2.0_det_infer\\"
)
setattr(
    fakeArgs, "e2e_char_dict_path",
    "D:\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\ppocr\\utils\\ic15_dict.txt"
) if not __work__ else setattr(
    fakeArgs, "e2e_char_dict_path",
    "D:\\github_repo\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\ppocr\\utils\\ic15_dict.txt"
)
setattr(
    fakeArgs, "image_dir",
    "D:\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\doc\\imgs\\11.jpg"
) if not __work__ else setattr(
    fakeArgs, "image_dir",
    "D:\\github_repo\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\doc\\imgs\\11.jpg"
)
setattr(
    fakeArgs, "rec_char_dict_path",
    "D:\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\ppocr\\utils\\ppocr_keys_v1.txt"
) if not __work__ else setattr(
    fakeArgs, "rec_char_dict_path",
    "D:\\github_repo\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\ppocr\\utils\\ppocr_keys_v1.txt"
)
setattr(
    fakeArgs, "rec_model_dir",
    "D:\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\interence\\ch_ppocr_server_v2.0_rec_infer\\"
) if not __work__ else setattr(
    fakeArgs, "rec_model_dir",
    "D:\\github_repo\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\interence\\ch_ppocr_server_v2.0_rec_infer\\"
)
setattr(
    fakeArgs, "vis_font_path",
    'D:\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\doc\\fonts\\simfang.ttf'
) if not __work__ else setattr(
    fakeArgs, "vis_font_path",
    'D:\\github_repo\\dev-tool-for-python\\pyImageTranslator\\PaddleOCR\\doc\\fonts\\simfang.ttf'
)

# 默认参数
setattr(fakeArgs, "cls_batch_num", 6)
setattr(fakeArgs, "cls_image_shape", '3, 48, 192')
setattr(fakeArgs, "cls_thresh", 0.9)
setattr(fakeArgs, "det_algorithm", 'DB')
setattr(fakeArgs, "det_db_box_thresh", 0.5)
setattr(fakeArgs, "det_db_thresh", 0.3)
setattr(fakeArgs, "det_db_unclip_ratio", 1.6)
setattr(fakeArgs, "det_east_cover_thresh", 0.1)
setattr(fakeArgs, "det_east_nms_thresh", 0.2)
setattr(fakeArgs, "det_east_score_thresh", 0.8)
setattr(fakeArgs, "det_limit_side_len", 960)
setattr(fakeArgs, "det_limit_type", 'max')

setattr(fakeArgs, "det_sast_nms_thresh", 0.2)
setattr(fakeArgs, "det_sast_polygon", False)
setattr(fakeArgs, "det_sast_score_thresh", 0.5)
setattr(fakeArgs, "drop_score", 0.5)
setattr(fakeArgs, "e2e_algorithm", 'PGNet')
setattr(fakeArgs, "e2e_limit_side_len", 768)
setattr(fakeArgs, "e2e_limit_type", 'max')
setattr(fakeArgs, "e2e_model_dir", None)
setattr(fakeArgs, "e2e_pgnet_polygon", True)
setattr(fakeArgs, "e2e_pgnet_score_thresh", 0.5)

setattr(fakeArgs, "e2e_pgnet_valid_set", 'totaltext')
setattr(fakeArgs, "enable_mkldnn", False)
setattr(fakeArgs, "gpu_mem", 500)
setattr(fakeArgs, "ir_optim", True)
setattr(fakeArgs, "label_list", ['0', '180'])
setattr(fakeArgs, "max_batch_size", 10)
setattr(fakeArgs, "max_text_length", 25)
setattr(fakeArgs, "process_id", 0)
setattr(fakeArgs, "rec_algorithm", 'CRNN')
setattr(fakeArgs, "rec_batch_num", 6)

setattr(fakeArgs, "rec_char_type", 'ch')
setattr(fakeArgs, "rec_image_shape", '3, 32, 320')
setattr(fakeArgs, "total_process_num", 1)
setattr(fakeArgs, "use_angle_cls", True)
setattr(fakeArgs, "use_dilation", False)
setattr(fakeArgs, "use_fp16", False)

setattr(fakeArgs, "use_gpu", False)
setattr(fakeArgs, "use_mp", False)
setattr(fakeArgs, "use_pdserving", False)
setattr(fakeArgs, "use_angle_cls", True)
setattr(fakeArgs, "use_space_char", True)
setattr(fakeArgs, "use_tensorrt", False)


def changeImgPath(imgpath: str):
    setattr(fakeArgs, 'image_dir', imgpath)
