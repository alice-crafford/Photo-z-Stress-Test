# Run the Test_Pipeline.ipynb thing here!! Need to configure it so that it outputs all of the files you need to run this 

## filename is a string containing the name of the .hdf5 file you want to convert
def hdf5_to_QPEns(filename):
    import h5py
    import qp
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
def toTable(datafile):
    import tables_io
    pq = col_remapper(datafile)
    tabledata = table_conv(pq)
    table = tables_io.convertObj(tabledata.data, tables_io.types.PD_DATAFRAME)
    return table

orig_train_table = toTable(orig_train)
deg_train_table = toTable(deg_train)

orig_test_table = toTable(orig_test)
deg_train_table = toTable(deg_test)


##takes the name of an .hdf5 file as a string 
def xvalsYvals(filename):
    import h5py
    f = h5py.File(filename, 'r')
    data = f['data']
    meta = f['meta']
    yvals = data['yvals']
    xvals = data['xvals']
    return [xvals, yvals]

##data is intended to be the output of xvalsYvals (list of arrays), dim is an int, 1 way dimension of # of plots you want 
def plotPosts(data, dim):
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(nrows = dim, ncols = dim, figsize = (4*dim, 2*dim)) 
    ct = 0
    for i in range(0, dim):
        for j in range(0, dim):
            axes[i][j].plot(data[0][0], data[1][ct])
            ct += 1