import csv
import h5py
import sys
import warnings

warnings.warn(
    "extra_data.h5index is deprecated and likely to be removed. "
    "If you are using it, please contact da-support@xfel.eu.",
    stacklevel=2,
)

def hdf5_datasets(grp):
    """Print CSV data of all datasets in an HDF5 file.

    path, shape, dtype
    """
    all_datasets = []

    def visitor(path, item):
        if isinstance(item, h5py.Dataset):
            all_datasets.append([path, item.shape, item.dtype.str])

    grp.visititems(visitor)

    writer = csv.writer(sys.stdout)
    writer.writerow(['path', 'shape', 'dtype'])
    for row in sorted(all_datasets):
        writer.writerow(row)


def main():
    file = h5py.File(sys.argv[1])
    hdf5_datasets(file)


if __name__ == '__main__':
    main()
