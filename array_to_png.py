import os
import matplotlib
path = '/home/prateek/image'
out_path = '/home/prateek/image_out/output/'
a = os.listdir(path)
print(a)
for i, name in enumerate(a):
    os.chdir(path + '/' + name)
    a = os.listdir(os.getcwd())
    os.mkdir(out_path + name)
    for i,img in enumerate(a):
        img1 = os.path.splitext(img)[0]
        path1 = os.getcwd() + "/" + img
        try:
            original_im = Image.open(path1)
        except IOError:
            print('Cannot retrieve image. Please check url: ')

        print('running deeplab on image %s...')
        resized_im, seg_map = MODEL.run(original_im)
        print(type(seg_map))
        '''
        vis_segmentation(resized_im, seg_map)
        im = Image.fromarray(seg_map)
        im.save(out_path + a + "/img" + "." + png)
        '''
        os.chdir(path + '/' + name)
        matplotlib.pyplot.imsave(out_path + name + "/" + img1 + ".png", seg_map, cmap="gray", vmin=0, vmax=255 )
