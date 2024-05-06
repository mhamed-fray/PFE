from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.stats import pearsonr
from django.shortcuts import render
import pandas as pd
import numpy as np
import pickle
# Create your views here.

def index(request):

    # Page from the theme 
     return render(request, 'pages/index.html')






   

     

    
   