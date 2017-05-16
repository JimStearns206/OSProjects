# Referenced in README_pandas_js206.md
## Python Version Used

```bash
python
Python 3.6.1 |Continuum Analytics, Inc.| (default, May 11 2017, 13:04:09) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```

<a name="CExtensionBuildOutput"></a>
## In-place build of C extensions

```bash

(pandas_dev3) [pandas-jimstearns206]$ python setup.py build_ext --inplace
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/setuptools-27.2.0-py3.6.egg/setuptools/dist.py:331: UserWarning: Normalizing '0.21.0.dev+31.g0ea0f25bf' to '0.21.0.dev0+31.g0ea0f25bf'
running build_ext
cythoning pandas/_libs/lib.pyx to pandas/_libs/lib.c
building 'pandas._libs.lib' extension
creating build
creating build/temp.macosx-10.7-x86_64-3.6
creating build/temp.macosx-10.7-x86_64-3.6/pandas
creating build/temp.macosx-10.7-x86_64-3.6/pandas/_libs
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/lib.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/lib.o -Wno-unused-function
In file included from pandas/_libs/lib.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
pandas/_libs/lib.c:100229:93: warning: code will never be executed [-Wunreachable-code]
        module = PyImport_ImportModule((PY_VERSION_HEX >= 0x03030000) ? "collections.abc" : "collections");
                                                                                            ^~~~~~~~~~~~~
pandas/_libs/lib.c:100229:59: note: silence by adding parentheses to mark code as explicitly dead
        module = PyImport_ImportModule((PY_VERSION_HEX >= 0x03030000) ? "collections.abc" : "collections");
                                                          ^
                                                          /* DISABLES CODE */ ( )
2 warnings generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/lib.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/lib.cpython-36m-darwin.so
cythoning pandas/_libs/hashtable.pyx to pandas/_libs/hashtable.c
building 'pandas._libs.hashtable' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/hashtable.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/hashtable.o -Wno-unused-function
In file included from pandas/_libs/hashtable.c:436:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
pandas/_libs/hashtable.c:28712:39: warning: self-comparison always evaluates to false [-Wtautological-compare]
            __pyx_t_16 = (__pyx_v_val != __pyx_v_val);
                                      ^
pandas/_libs/hashtable.c:32190:39: warning: self-comparison always evaluates to false [-Wtautological-compare]
            __pyx_t_16 = (__pyx_v_val != __pyx_v_val);
                                      ^
3 warnings generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/hashtable.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/hashtable.cpython-36m-darwin.so
cythoning pandas/_libs/tslib.pyx to pandas/_libs/tslib.c
building 'pandas._libs.tslib' extension
creating build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src
creating build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/tslib.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/tslib.o -Wno-unused-function
In file included from pandas/_libs/tslib.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
pandas/_libs/tslib.c:32529:17: warning: implicit declaration of function 'cmp_pandas_datetimestruct' is invalid
      in C99 [-Wimplicit-function-declaration]
  __pyx_t_2 = ((cmp_pandas_datetimestruct(__pyx_v_dts, (&__pyx_v_6pandas_5_libs_5tslib__NS_MIN_DTS)) == -...
                ^
2 warnings generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/datetime/np_datetime.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime.o -Wno-unused-function
In file included from pandas/_libs/src/datetime/np_datetime.c:22:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/datetime/np_datetime_strings.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime_strings.o -Wno-unused-function
In file included from pandas/_libs/src/datetime/np_datetime_strings.c:29:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/period_helper.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/period_helper.o -Wno-unused-function
In file included from pandas/_libs/src/period_helper.c:16:
In file included from pandas/_libs/src/period_helper.h:21:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/tslib.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime_strings.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/period_helper.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/tslib.cpython-36m-darwin.so
cythoning pandas/_libs/period.pyx to pandas/_libs/period.c
building 'pandas._libs.period' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/period.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/period.o -Wno-unused-function
In file included from pandas/_libs/period.c:436:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/datetime/np_datetime.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime.o -Wno-unused-function
In file included from pandas/_libs/src/datetime/np_datetime.c:22:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/datetime/np_datetime_strings.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime_strings.o -Wno-unused-function
In file included from pandas/_libs/src/datetime/np_datetime_strings.c:29:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/period_helper.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/period_helper.o -Wno-unused-function
In file included from pandas/_libs/src/period_helper.c:16:
In file included from pandas/_libs/src/period_helper.h:21:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/period.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime_strings.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/period_helper.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/period.cpython-36m-darwin.so
cythoning pandas/_libs/index.pyx to pandas/_libs/index.c
building 'pandas._libs.index' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/index.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/index.o -Wno-unused-function
In file included from pandas/_libs/index.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/datetime/np_datetime.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime.o -Wno-unused-function
In file included from pandas/_libs/src/datetime/np_datetime.c:22:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/datetime/np_datetime_strings.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime_strings.o -Wno-unused-function
In file included from pandas/_libs/src/datetime/np_datetime_strings.c:29:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/index.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime_strings.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/index.cpython-36m-darwin.so
cythoning pandas/_libs/algos.pyx to pandas/_libs/algos.c
building 'pandas._libs.algos' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/algos.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/algos.o -Wno-unused-function
In file included from pandas/_libs/algos.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/algos.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/algos.cpython-36m-darwin.so
cythoning pandas/_libs/groupby.pyx to pandas/_libs/groupby.c
building 'pandas._libs.groupby' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/groupby.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/groupby.o -Wno-unused-function
In file included from pandas/_libs/groupby.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/groupby.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/groupby.cpython-36m-darwin.so
cythoning pandas/_libs/join.pyx to pandas/_libs/join.c
building 'pandas._libs.join' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/join.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/join.o -Wno-unused-function
In file included from pandas/_libs/join.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/join.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/join.cpython-36m-darwin.so
cythoning pandas/_libs/reshape.pyx to pandas/_libs/reshape.c
building 'pandas._libs.reshape' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/reshape.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/reshape.o -Wno-unused-function
In file included from pandas/_libs/reshape.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/reshape.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/reshape.cpython-36m-darwin.so
cythoning pandas/_libs/interval.pyx to pandas/_libs/interval.c
building 'pandas._libs.interval' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/interval.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/interval.o -Wno-unused-function
In file included from pandas/_libs/interval.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/interval.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/interval.cpython-36m-darwin.so
cythoning pandas/_libs/window.pyx to pandas/_libs/window.c
building 'pandas._libs.window' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/window.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/window.o -Wno-unused-function
In file included from pandas/_libs/window.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/window.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/window.cpython-36m-darwin.so
cythoning pandas/_libs/parsers.pyx to pandas/_libs/parsers.c
building 'pandas._libs.parsers' extension
creating build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/parser
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/parsers.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/parsers.o -Wno-unused-function
In file included from pandas/_libs/parsers.c:437:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/parser/tokenizer.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/parser/tokenizer.o -Wno-unused-function
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/parser/io.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/parser/io.o -Wno-unused-function
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/parsers.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/parser/tokenizer.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/parser/io.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/parsers.cpython-36m-darwin.so
cythoning pandas/_libs/sparse.pyx to pandas/_libs/sparse.c
building 'pandas._libs.sparse' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/sparse.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/sparse.o -Wno-unused-function
In file included from pandas/_libs/sparse.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/sparse.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/sparse.cpython-36m-darwin.so
cythoning pandas/_libs/testing.pyx to pandas/_libs/testing.c
building 'pandas._libs.testing' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/testing.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/testing.o -Wno-unused-function
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/testing.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/testing.cpython-36m-darwin.so
cythoning pandas/_libs/hashing.pyx to pandas/_libs/hashing.c
warning: pandas/_libs/hashing.pyx:45:13: Non-trivial type declarators in shared declaration (e.g. mix of pointers and values). Each pointer declaration should be on its own line.
warning: pandas/_libs/hashing.pyx:45:21: Non-trivial type declarators in shared declaration (e.g. mix of pointers and values). Each pointer declaration should be on its own line.
building 'pandas._libs.hashing' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/hashing.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/hashing.o -Wno-unused-function
In file included from pandas/_libs/hashing.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/hashing.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/hashing.cpython-36m-darwin.so
cythoning pandas/io/sas/sas.pyx to pandas/io/sas/sas.c
building 'pandas.io.sas._sas' extension
creating build/temp.macosx-10.7-x86_64-3.6/pandas/io
creating build/temp.macosx-10.7-x86_64-3.6/pandas/io/sas
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/io/sas/sas.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/io/sas/sas.o -Wno-unused-function
In file included from pandas/io/sas/sas.c:435:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/io/sas/sas.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/io/sas/_sas.cpython-36m-darwin.so
cythoning pandas/io/msgpack/_packer.pyx to pandas/io/msgpack/_packer.cpp
building 'pandas.io.msgpack._packer' extension
creating build/temp.macosx-10.7-x86_64-3.6/pandas/io/msgpack
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -D__LITTLE_ENDIAN__=1 -Ipandas/_libs/src/msgpack -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/io/msgpack/_packer.cpp -o build/temp.macosx-10.7-x86_64-3.6/pandas/io/msgpack/_packer.o -Wno-unused-function
pandas/io/msgpack/_packer.cpp:3373:13: warning: code will never be executed [-Wunreachable-code]
  __pyx_r = 0;
            ^
1 warning generated.
g++ -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/io/msgpack/_packer.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/io/msgpack/_packer.cpython-36m-darwin.so
clang: warning: libstdc++ is deprecated; move to libc++ with a minimum deployment target of OS X 10.9 [-Wdeprecated]
cythoning pandas/io/msgpack/_unpacker.pyx to pandas/io/msgpack/_unpacker.cpp
building 'pandas.io.msgpack._unpacker' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -D__LITTLE_ENDIAN__=1 -Ipandas/_libs/src/msgpack -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/io/msgpack/_unpacker.cpp -o build/temp.macosx-10.7-x86_64-3.6/pandas/io/msgpack/_unpacker.o -Wno-unused-function
pandas/io/msgpack/_unpacker.cpp:2270:31: warning: comparison of integers of different signs: 'size_t'
      (aka 'unsigned long') and 'Py_ssize_t' (aka 'long') [-Wsign-compare]
    __pyx_t_2 = ((__pyx_v_off < __pyx_v_buf_len) != 0);
                  ~~~~~~~~~~~ ^ ~~~~~~~~~~~~~~~
pandas/io/msgpack/_unpacker.cpp:4288:19: warning: comparison of integers of different signs: 'size_t'
      (aka 'unsigned long') and 'Py_ssize_t' (aka 'long') [-Wsign-compare]
  if (((__pyx_t_2 < __pyx_t_3) != 0)) {
        ~~~~~~~~~ ^ ~~~~~~~~~
pandas/io/msgpack/_unpacker.cpp:4962:19: warning: comparison of integers of different signs: 'Py_ssize_t'
      (aka 'long') and 'size_t' (aka 'unsigned long') [-Wsign-compare]
  if (((__pyx_t_1 < __pyx_t_2) != 0)) {
        ~~~~~~~~~ ^ ~~~~~~~~~
3 warnings generated.
g++ -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/io/msgpack/_unpacker.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/io/msgpack/_unpacker.cpython-36m-darwin.so
clang: warning: libstdc++ is deprecated; move to libc++ with a minimum deployment target of OS X 10.9 [-Wdeprecated]
building 'pandas._libs.json' extension
creating build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson
creating build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/python
creating build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/lib
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/ujson/python -Ipandas/_libs/src/ujson/lib -Ipandas/_libs/src/datetime -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/ujson/python/ujson.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/python/ujson.o -D_GNU_SOURCE -Wno-unused-function
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/ujson/python -Ipandas/_libs/src/ujson/lib -Ipandas/_libs/src/datetime -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/ujson/python/objToJSON.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/python/objToJSON.o -D_GNU_SOURCE -Wno-unused-function
In file included from pandas/_libs/src/ujson/python/objToJSON.c:44:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/ujson/python -Ipandas/_libs/src/ujson/lib -Ipandas/_libs/src/datetime -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/ujson/python/JSONtoObj.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/python/JSONtoObj.o -D_GNU_SOURCE -Wno-unused-function
In file included from pandas/_libs/src/ujson/python/JSONtoObj.c:44:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/ujson/python -Ipandas/_libs/src/ujson/lib -Ipandas/_libs/src/datetime -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/ujson/lib/ultrajsonenc.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/lib/ultrajsonenc.o -D_GNU_SOURCE -Wno-unused-function
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/ujson/python -Ipandas/_libs/src/ujson/lib -Ipandas/_libs/src/datetime -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/ujson/lib/ultrajsondec.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/lib/ultrajsondec.o -D_GNU_SOURCE -Wno-unused-function
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/ujson/python -Ipandas/_libs/src/ujson/lib -Ipandas/_libs/src/datetime -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/datetime/np_datetime.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime.o -D_GNU_SOURCE -Wno-unused-function
In file included from pandas/_libs/src/datetime/np_datetime.c:22:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -Ipandas/_libs/src/ujson/python -Ipandas/_libs/src/ujson/lib -Ipandas/_libs/src/datetime -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/_libs/src/datetime/np_datetime_strings.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime_strings.o -D_GNU_SOURCE -Wno-unused-function
In file included from pandas/_libs/src/datetime/np_datetime_strings.c:29:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/ndarraytypes.h:1788:
/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning: 
      "Using deprecated NumPy API, disable it by "          "#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
      [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/python/ujson.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/python/objToJSON.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/python/JSONtoObj.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/lib/ultrajsonenc.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/ujson/lib/ultrajsondec.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime.o build/temp.macosx-10.7-x86_64-3.6/pandas/_libs/src/datetime/np_datetime_strings.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/_libs/json.cpython-36m-darwin.so
building 'pandas.util._move' extension
creating build/temp.macosx-10.7-x86_64-3.6/pandas/util
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/include -arch x86_64 -I/Users/jimstearns/anaconda/envs/pandas_dev3/lib/python3.6/site-packages/numpy/core/include -I/Users/jimstearns/anaconda/envs/pandas_dev3/include/python3.6m -c pandas/util/move.c -o build/temp.macosx-10.7-x86_64-3.6/pandas/util/move.o
gcc -bundle -undefined dynamic_lookup -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -arch x86_64 build/temp.macosx-10.7-x86_64-3.6/pandas/util/move.o -L/Users/jimstearns/anaconda/envs/pandas_dev3/lib -o /Users/jimstearns/NoCloudDrive/Learning/OSProjects/pandas-jimstearns206/pandas/util/_move.cpython-36m-darwin.so
(pandas_dev3) [pandas-jimstearns206]$ 
```
