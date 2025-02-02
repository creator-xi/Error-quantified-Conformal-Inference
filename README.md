# Error-quantified Conformal Inference


**This repository contains the data and code required to reproduce the results in ICLR2025 paper "Error-quantified Conformal Inference for Time Series"**, where we borrow or extend some code from [PID](https://github.com/aangelopoulos/conformal-time-series/tree/main).



## Environment
<p>
Please clone this repo and run following command locally for install the environment:
<pre>
conda create --name eci
pip install -r requirements.txt
</pre>
</p>



## Demo

Please run following command locally for local test:
<pre>
cd tests
python base_test.py configs/AMZN_test.yaml
python base_plots.py results/AMZN_test.pkl
</pre>

The plot results will be saved in <code>test/plots</code> folder. More commands can be seen in <code>tests/expbook.ipynb</code>. Users can modify the YAML files in the <code>configs</code> folder to configure the experimental settings.



### Citation
If you find this work useful, you can cite it with the following BibTex entry:

    @inproceedings{wu2025error,
      title={Error-quantified Conformal Inference for Time Series},
      author={Wu, Junxi and Hu, Dongjian and Bao, Yajie and Xia, Shu-tao and Zou, Changliang},
      booktitle={The Thirteenth International Conference on Learning Representations},
      year={2025}
    }
