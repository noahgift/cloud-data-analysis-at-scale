

### Exercise:  Sagemaker Scavenger Hunt

* Topic:  Build a Sagemaker based Data Science project
* Estimated time:  45 minutes
* People:  Individual or Final Project Team
* Slack Channel:  #noisy-exercise-chatter
* Directions:

* Part A:  Get the [airline data](https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/CUR-TF-200-ACBDFO-1/Lab5/flightdata.csv) into your own Sagemaker.
* Part B:  Performance the Data Science worflow:
    - Ingest: Process the data
    - EDA: Visualize and Explore data
    - Model:  Create some form of a model
    - Conclusion
* Part C:  Consider trying multiple visualization libraries:  [Plotly](https://plot.ly/), Vega, Bokeh and Seaborn
* Part D:  Download notebook and upload into Colab, then check notebook in a Github porfolio repo.
*Hints: You may want to truncate the data and upload a small version into Github using unix `shuf` command.

```bash
shuf -n 100000 en.openfoodfacts.org.products.tsv\
> 10k.sample.en.openfoodfacts.org.products.tsv
1.89s user 0.80s system 97% cpu 2.748 total
```
