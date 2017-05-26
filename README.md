# CycleGAN Production Version

> this repo based on the original implementation of CycleGAN: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git, in this version I reconstruct some code and made a generate API to simply generate image from your own single image and your trained model.

# CycleGAN - Generate Image Like Magic

I have trained `apple2orange` and `horse2zebra` for now, here is the real result of convert
apple -> orange:



<img align="center" src="http://ofwzcunzi.bkt.clouddn.com/Re7W22VtZtgEQSQ9.png"></img>



<img align="center" src="http://ofwzcunzi.bkt.clouddn.com/7ECiF3alBHYkPj3o.png"></img>



<img align="center" src="http://ofwzcunzi.bkt.clouddn.com/yEEM3RcADYp5YvfZ.png"></img>

I only trained about 50 epochs, but the result is fair enough for now. Laterly I will finish horse2zebra model, and update some more results.

Here is the horse2zebra result:

![PicName](http://ofwzcunzi.bkt.clouddn.com/Q7UYP9ywezFOFvSy.png)

![PicName](http://ofwzcunzi.bkt.clouddn.com/GzIkgZcRlBl1WrmT.png)

# Requirements

* Python3+
* PyTorch
* visdom
* PIL

# Usage

* For Train

About how to train, simply run this:

```
python3 train.py --dataroot ./datasets/apple2orange --name apple2orange --model cycle_gan
```

One things have to mention that, `--name` indicates the model save dir, and `--model` is using `cycle_gan` or `pixel2pixel` , I only tried `cycle_gan`.

* For Generate

Train is very simple, but the original repo have not implement predict API, so I managed to write by myself. Here is the way to use:

```
python3 generate.py --image_path ./apple_test.jpg --name apple2orange --model cycle_gan --gpu_ids -1
```

As you can see, you only need to specific image path where stores your image to generate, and `--name` is the same as previous trained, as well as model type. `--gpu_ids` indicates we are inference using CPU.

OK, that's all.

# Research and Discuss

I really love to connect to people, so if you have any question about this repo, you can find me on wechat `jintianiloveu`, I have some groups which discuss about GANs I will invite you in if you like.

# Copyright

```
(c) 2017 Jin Fagang under LICENSE Apache 2.0
```
