import numpy as np
import pandas as pd

def csv2df(csv_path):
    df = pd.read_csv(csv_file_path)
    return df


def overlap_APs(fi,fj):
    fi_mask = (fi > 0.0)
    fj_mask = (fj > 0.0)
    overlap_array_mask = np.array((fi_mask & fj_mask).to_list())
    return overlap_array_mask


def detection_likelihood(fi, fj):
    # Take numbers of APs for each FP
    Li = fi['num_APs']
    Lj = fj['num_APs']
    # We just need list of RSS of each AP
    fi = fi.iloc[[0,1,2]]
    fj = fj.iloc[[0,1,2]]
    H = np.sum(overlap_APs(fi,fj))
    dl = np.divide(H, Li + Lj - H)
    return dl


def signal_strength_likelihood(fi, fj):
    sigma = 0.3
    fi = fi.iloc[[0,1,2]]
    fj = fj.iloc[[0,1,2]]
    overlap_array_mask = overlap_APs(fi, fj)
    overlap_indices = np.where(overlap_array_mask)[0]
    H = np.sum(overlap_array_mask)
    prod = 1.0
    for idx in overlap_indices:
        a = np.power(fi.iloc[idx] - fj.iloc[idx], 2)
        b = np.divide(a, 2*np.power(sigma,2))
        c = np.exp(-b)
        prod = prod * c
    
    ssl = np.divide(prod, H)
    return ssl




