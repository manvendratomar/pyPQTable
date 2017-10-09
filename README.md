# pyPQTable

**Python wrapper of PQTable** (https://github.com/matsui528/pqtable.git)

**Product Quantization Table (PQTable)** is a fast nearest neighbor search method for product-quantized codes via hash-tables. PQTable achieves one of the fastest search performances on a single CPU to date (2017) with significantly efficient memory usage (0.059 ms per query over
10^9 data points with just 5.5 GB memory consumption).

References:

- Project page: [http://yusukematsui.me/project/pqtable/pqtable.html](http://yusukematsui.me/project/pqtable/pqtable.html)

## Building

Requisites:
* C++11
* CMake
* OpenCV 3.X
* [TCMalloc](http://goog-perftools.sourceforge.net/doc/tcmalloc.html) (optional, but strongly recommended). On ubuntu, you can install TCMalloc by `sudo apt-get install libgoogle-perftools-dev`. Then link it via the "-ltcmalloc" linker flag. This makes the search ~2x faster.
* swig

Build as usual with CMake:
```
$ git clone https://github.com/matsui528/pqtable.git
$ cd pqtable
$ swig -c++ -python pqtable.i
$ python setup.py install
```

## Testing
### Demo using the siftsmall dataset
You can try a small demo using the siftsmall data. This does not take time.
First, `cd` to the top directory of this project, then download the siftsmall vectors on `data/`.
```
$ bash scripts/download_siftsmall.sh 
```

```
$ python demo_siftsmall.py
```
The program trains a product-quantizer, encodes vectors, builds PQTable, and runs the search. The final results will be somthing like:

```
...
90th query: nearest_id=9258, dist=14886.5
91th query: nearest_id=6269, dist=90768.796875
92th query: nearest_id=4684, dist=73483.109375
93th query: nearest_id=4910, dist=51847.1328125
94th query: nearest_id=8419, dist=51929.84765625
95th query: nearest_id=9682, dist=78979.2890625
96th query: nearest_id=7512, dist=67794.765625
97th query: nearest_id=5941, dist=60799.1640625
98th query: nearest_id=5711, dist=18704.76171875
0.2281954794219046 [msec/query]
```







