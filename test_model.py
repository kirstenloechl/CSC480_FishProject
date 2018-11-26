import label_image

import argparse

import numpy as np
import random

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

import tensorflow as tf

fish_lut = {
    'fish_01': 'Dascyllus reticulatus',
    'fish_02': 'Plectroglyphidodon dickii',
    'fish_03': 'Chromis chrysura',
    'fish_04': 'Amphiprion clarkii',
    'fish_05': 'Chaetodon lunmulatus',
    'fish_06': 'Chaetodon trifascialis',
    'fish_07': 'Myripristis kuntee',
    'fish_08': 'Acanthurus nigrofuscus',
    'fish_09': 'Hemigymnus fasciatus',
    'fish_10': 'Neoniphon sammara',
    'fish_11': 'Abudefduf vaigiensis',
    'fish_12': 'Canthigaster valentini',
    'fish_13': 'Pomacentru moluccensis',
    'fish_14': 'Zebrasoma scopas',
    'fish_15': 'Hemigymnus melapterus',
    'fish_16': 'Lutjanus fulvus',
    'fish_17': 'Scolopsis bilineata',
    'fish_18': 'Scaridae',
    'fish_19': 'Pempheris vanicolensis',
    'fish_20': 'Zanclus cornutus',
    'fish_21': 'Neoglyphidodon nigrosis',
    'fish_22': 'Balistapus undulatus',
    'fish_23': 'Siganus fuscescens',
}


def getDirectories(direc):
    return [os.path.join(direc, f) for f in os.listdir(direc)
            if os.path.isdir(os.path.join(direc, f))]


def getFiles(direc):
    return [os.path.join(direc, f) for f in os.listdir(direc)
            if os.path.isfile(os.path.join(direc, f))]


def getRandomSet(direc):
    return [random.choice(getFiles(s)) for s in getDirectories(direc)]


def loadImage(filepath,
              model_file='output_graph.pb',
              label_file='output_labels.txt',
              input_height=299,
              input_width=299,
              input_mean=0,
              input_std=255,
              input_layer='Placeholder',
              output_layer='final_result'):

    graph = label_image.load_graph(model_file)
    t = label_image.read_tensor_from_image_file(
        filepath,
        input_height=input_height,
        input_width=input_width,
        input_mean=input_mean,
        input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    with tf.Session(graph=graph) as sess:
        results = sess.run(output_operation.outputs[0], {
            input_operation.outputs[0]: t
        })

    results = np.squeeze(results)

    bestGuess = results.argsort()[-1]

    labels = label_image.load_labels(label_file)
    actName = filepath.split('/')[-2]

    plt.cla()

    ax = plt.axes()
    ax.set_title('Predicted: ' + fish_lut[labels[bestGuess]] +
                 '\nActual: ' + fish_lut[actName] +
                 '\nConfidence: ' + str(results[bestGuess]))

    plt.imshow(mpimg.imread(filepath))

    plt.draw()


imgs = []
imageIndex = 0
args = {}


def onclick(event):
    global imageIndex
    global imgs
    global args

    loadImage(imgs[imageIndex], model_file=args.graph, label_file=args.labels)
    imageIndex += 1

    if imageIndex == len(imgs):
        imgs = getRandomSet(args.data)
        imageIndex = 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--graph', help='model to be used', required=True)
    parser.add_argument('--labels', help='text file containing labels',
                        required=True)
    parser.add_argument('--data', help='top level folder of images',
                        required=True)

    args = parser.parse_args()

    imgs = getRandomSet(args.data)

    fig = plt.figure()
    fig.canvas.mpl_connect('button_press_event', onclick)

    loadImage(imgs[imageIndex], model_file=args.graph, label_file=args.labels)
    imageIndex += 1

    plt.show()
