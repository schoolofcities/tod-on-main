# Newer-Models

The only important thing from here is that the useful functions for feature engineering is in ```useful_functions.ipynb```

I also recommend removing a lot of the columns that have correlation as this effects the interpretability of each of the columns and its effect on the output. Finally, I have tested using both 'before' and 'after' columns or using the 'change' ('after' - 'before'). Both have some success and some failure.

The best model was XGBOOST but might have large overfitting issues so try more simple statistical or ML models (like simple linear regression)

The best notebook to look at how to build some models is ```final_models.ipynb```

### Findings
- The models work with varying success.
- The best models were XGBRegressor or Random Forest (but risk of overfitting)
- I think a better method is the use simple models and try improve it through feature engineering and hyperparameter tuning
- We can also try adding synthetic data, but this didn't have much success
- Another issue is there are many columns and not many rows - causes overfitting and increased variance
- There is a lot of correlation and collinearity in the columns - so try find some to remove (e.g. rented + owned is approximately total dwellings)
- Use the VIF (variance inflation factor) to see which columns have a lot of correlation and removing those (have not finished testing different combinations of this)