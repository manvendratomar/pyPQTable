%module pqtable
%{
#define SWIG_PYTHON_EXTRA_NATIVE_CONTAINERS
#define SWIG_FILE_WITH_INIT
#include "src/pq.h"
#include "src/pq_table.h"
#include "src/sparse_hashtable/sparse_hashtable.h"
#include "src/sparse_hashtable/bucket_group.h"
#include "src/sparse_hashtable/array32.h"
#include "src/sparse_hashtable/helper_sht.h"
#include "src/sparse_hashtable/types.h"
#include "src/pq_key_generator.h"
#include "src/code_to_key.h"
#include "opencv2/opencv.hpp"
#include "src/utils.h"
#include <cstdio>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
%}


%include "std_vector.i"
%include "std_pair.i"

namespace std{
    %template(FloatVector) vector<float>;
    %template(Array) vector<vector<float> >;
    %template(ArrayVector) vector<vector<vector<float> > >;
    %template(PairIntFloat) pair<int, float>;
}


%rename(__assign__) Array32::operator=;
%rename(print_array) Array32::print();
%rename(Encode_Array) pqtable::PQ::Encode(const std::vector<std::vector<float> > &vecs) const;

%include <std_string.i>
%include "std_string.i"
%include "std_basic_string.i"
%include "cstring.i"
%include "std_char_traits.i"
%include "std_iostream.i"
%include "std_alloc.i"
%include "cmalloc.i"
%include "src/pq.h"
%include "src/pq_table.h"
%include "src/sparse_hashtable/sparse_hashtable.h"
%include "src/sparse_hashtable/bucket_group.h"
%include "src/sparse_hashtable/array32.h"
%include "src/sparse_hashtable/helper_sht.h"
%include "src/sparse_hashtable/types.h"
%include "src/pq_key_generator.h"
%include "src/utils.h"
%include "src/code_to_key.h"

