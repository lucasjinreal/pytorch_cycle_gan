"""
usage:
python3 generate.py --image_path ./apple_test.jpg --name apple2orange --model cycle_gan --gpu_ids -1

gpu_ids: -1 for cpu inference
"""
from options.test_options import TestOptions
opt = TestOptions().parse()
from models.one_direction_test_model import OneDirectionTestModel
from data.unaligned_data_loader import load_image_for_prediction
import sys
import cv2
import os
import numpy as np
from PIL import Image

opt.nThreads = 1
opt.batchSize = 1
opt.serial_batches = True


def generate():
    """
    generate single image specific by image path, and show the after generated image
    :return:
    """
    image_path = opt.image_path
    print('generate from {}'.format(image_path))

    data = load_image_for_prediction(opt, image_path)

    model = OneDirectionTestModel()
    model.initialize(opt=opt)
    model.set_input(data)
    model.test()

    visuals = model.get_current_visuals()
    generated_a = visuals['fake_B']

    image_generated = Image.fromarray(generated_a)
    image_generated.save(str(os.path.basename(image_path).split('.')[0]) + '_fake_b.jpg')

    combined_result = np.concatenate([img for _, img in visuals.items()], 1)
    image_combined = Image.fromarray(combined_result)
    image_combined.save(str(os.path.basename(image_path).split('.')[0]) + '_combined.jpg')
    image_combined.show()
    print('generated image saved.')



if __name__ == '__main__':
    generate()

