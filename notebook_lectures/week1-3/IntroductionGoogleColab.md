## Introduction to Google Colab

Google cloud's version of Jupyter notebook where you have access to resources for free.

You need to have a google account for this. After that you can go to

https://colab.research.google.com/

You can sign in into your account on the **top-right login link**.

To create a new notebook, go to file and click on New python 3 notebook

Your browser will open a new window for this.

Jupyter notebooks created in Google colab are saved into your google drive. If you want to see where it is located, you can click on file and then locate in drive. You are going to see that the notebooks will be saved in your google colab notebook. If you want to open a notebook while you are in your drive, click on your mouse right boton. A menu will show up, click in more and then choose google collaboratory. 

You will notice that your google colab interface is very similar to the one from Jupyter notebook. Basically google colab offer a very similar environment, where most packages are installed and if they are not, you can installed yourself. 

In the google colab notebook, you can input Python commands and run them with 

```
<shift>-<enter>
```



If you want to open a new cell 

```
<control>-m-b
```



If you want to change the cell type to "text" by using markdown  

```
<control>-m-m
```

and if you want to return to "code cell", use

```
<control>-m-y
```

To write text in the colab, you have seen that you can use markdown, which is a very simple languate to write text. For example, if you want a title use #title.

Now it is important to keep in mind that everything you run into the google colab is run remotely in a machine is own by google. This means that you do not need to have Python installed in your machine. 

If you go to runtime, you can change from python 2 to python 3 and you can also change the processor from a CPU to GPU. The default has 13Gb of RAM but it is not GPU, the GPU has a Tesla KAGPU and the same memory.  There is another option, which is TPU, which is a tensor processing unit (no many codes support this time of processing, but that will change in the future).

If you want to import some data into your google colab, that data has to be in your google drive, which then you need to "load this drive" into your notebook, for that use:

```
from google.colab import drive
drive.mount('gdrive')
```

You will have to authorize it by clicking in the link that is returned and follow the instructions. You know that it has been loaded if you click in "files" and you see the mounted "drive"

Now you can upload files that you have in your google drive by

```
myfile = open('gdrive/My Drive/Chengsdata/ysensor1.csv')
```

You can also run bash commands within your cell.  This can be done by prepend the line with !

for example

```
!ls 'gdrive/My Drive/Chengsdata'
```

You can also use this command to install packages that are not installed originally in the colab instance. For example

```
!pip install tensorflow==2
```

After installation is done, you need to make the notebook aware of this, which is done by clicking on runtime and then restart runtime. 

To check if what you have imported is now recognized, you can use the command

```
import tensorflow as tf
tf.__version__
```

Additionally, google colab can also open a Jupiter notebook that is in your local machine. For that, go to file and then upload notebook. Even you happen to have your own Github, you can also uploaded here. 

If you want to download you google colab notebook as a jupyter notebook. You go to files and then "download as .ipynb"

If you want to learn more from Google colab, you can go to the link

https://colab.research.google.com/notebooks/welcome.ipynb