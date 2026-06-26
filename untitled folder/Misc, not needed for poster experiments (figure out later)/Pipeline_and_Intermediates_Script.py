# Run the Test_Pipeline.ipynb thing here!! Need to configure it so that it outputs all of the files you need to run this 

## filename is a string containing the name of the .hdf5 file you want to convert
def hdf5_to_QPEns(filename):
    import h5py
    import qp
    import os
    import rail
    #from rail.evaluation.metrics.cdeloss import *
    from rail.evaluation.evaluator import Evaluator
    from rail.core.data import QPHandle, TableHandle
    from rail.core.stage import RailStage
    #from rail.evaluation.utils import plot_pit_qq, ks_plot
    # %matplotlib inline
    # %reload_ext autoreload
    # %autoreload 2

    DS = RailStage.data_store
    DS.__class__.allow_overwrite = True
  
    f = DS.read_file('pdfs_data', QPHandle, filename)
    f_yvals = f().objdata()['yvals']
    f_xvals = f().metadata()['xvals'][0]
    ens = qp.Ensemble(qp.interp, data=dict(xvals=f_xvals, yvals=f_yvals))
    return ens 

orig_train_ens = hdf5_to_QPEns('output_orig_train_posts')
deg_train_ens = hdf5_to_QPEns('output_deg_train_posts')
orig_test_ens = hdf5_to_QPEns('output_orig_test_posts')
deg_test_ens = hdf5_to_QPEns('output_deg_test_posts')

## turn an array or datahandle into a tables.io file, datafile is one of these datastructures, *not* a string name 
def makeTable(datafile):
    import tables_io
    pq = col_remapper(datafile)
    tabledata = table_conv(pq)
    table = tables_io.convertObj(tabledata.data, tables_io.types.PD_DATAFRAME)
    return table

orig_train_table = makeTable(orig_train)
deg_train_table = makeTable(deg_train)

orig_test_table = makeTable(orig_test)
deg_train_table = makeTable(deg_test)


##takes a list of the names of .hdf5 files as a strings 
def xvalsYvals(filenames):
    ls = []
    import h5py
    for i in filenames:
        f = h5py.File(i, 'r')
        data = f['data']
        meta = f['meta']
        yvals = data['yvals']
        xvals = meta['xvals']
        ls.append([xvals, yvals])
    return ls

##data is intended to be the output of xvalsYvals (2D list of arrays), dim is an int, 1 way dimension of # of plots you want 
def plotPosts(data, dim):
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(nrows = dim, ncols = dim, figsize = (4*dim, 2*dim)) 
    ct = 0
    for i in data:
        for j in range(0, dim):
            for k in range(0, dim):
                axes[j][k].plot(i[0][0], i[1][ct])
                ct += 1

##helpful for plotting data in each magnitude band, takes a list of outputs of makeTables 
def plotMags(tables):
    import numpy as np
    for j in tables:
        data = np.asarray(j)
        redshift = data[:,0]
        u = data[:, 1]
        g = data[:, 2]
        r = data[:, 3]
        i = data[:, 4]
        z = data[:, 5]
        y = data[:, 6]