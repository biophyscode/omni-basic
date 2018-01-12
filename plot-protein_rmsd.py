#!/usr/bin/env python

# settings
plotname = 'protein_rmsd'
rmsd_bin_step = 0.1
# load the upstream dat
data,calc = plotload(plotname,work)
# make the plot
axes,fig = square_tiles(1,figsize=(12,8))
counter,xpos,xlim_left = 0,[],0
max_rmsd = max([max(data[sn]['data']['rmsds']) for sn in data])
rmsd_bins = np.arange(0,max_rmsd*1.1,0.1)
for snum,sn in enumerate(data):
	ax = axes[0]
	ts = np.array(data[sn]['data']['timeseries'])
	rmsds = data[sn]['data']['rmsds']
	ts -= ts.min()
	ts = ts/1000. # convert to ns
	# set proper names inside the `meta` section of the metadata
	name_label = ' '.join(work.meta.get(sn,{}).get('name',sn).split('_'))
	ax.plot(ts,rmsds,label=name_label,lw=2)
	ax.set_xlabel(r'time (ns)')
	ax.set_ylim(0,max_rmsd*1.1)
	ax.set_ylabel(r'RMSD ($\mathrm{\AA}$)')
# save the figure to disk along with metadata if desired
picturesave('fig.%s'%plotname,work.plotdir,
	backup=False,version=True,meta={})
