def classifier_local_fidelity(shap_Series_clfier):
    """
    This function plots the local fidelity for the classifier model.
    This is useful in understanding the model output.

    """
    import matplotlib.pyplot as plt
    
    fig,ax = plt.subplots(figsize=(16,8))
    fig.patch.set_facecolor('#212121')
    fig.patch.set_alpha(0.95)

    ax.patch.set_facecolor('#212121')
    ax.patch.set_alpha(1.0)
    ax.yaxis.label.set_color('lime')
    ax.xaxis.label.set_color('lime')
    ax.title.set_color('lime')
    ax.tick_params(colors='lime', which='both')

    pos_val = shap_Series_clfier > 0

    shap_Series_clfier.plot(ax=ax,
                    kind='barh',
                    color= pos_val.map({True:'lime', False: 'red'}),
                    fontsize=12
                   )
    plt.grid()
    plt.title('Local explaination for classifier instance:\nPredicting less than 5 shopping trips per week', fontsize=18)
    plt.show()


def regressor_local_fidelity(shap_Series_regress):

    """
    This function plots the local explaination for the classifier model.
    This is useful in understanding the model output.
    
    """

    import matplotlib.pyplot as plt
    fig,ax = plt.subplots(figsize=(16,8))
    fig.patch.set_facecolor('#212121')
    fig.patch.set_alpha(0.95)

    ax.patch.set_facecolor('#212121')
    ax.patch.set_alpha(1.0)
    ax.yaxis.label.set_color('lime')
    ax.xaxis.label.set_color('lime')
    ax.title.set_color('lime')
    ax.tick_params(colors='lime', which='both')

    pos_val = shap_Series_regress > 0

    shap_Series_regress.plot(ax=ax,
                    kind='barh',
                    color= pos_val.map({True:'lime', False: 'red'}),
                    fontsize=12
                   )
    plt.grid()
    plt.title('Local explaination for regressor instance:\nPredicting expenditure per week', fontsize=18)
    plt.show()