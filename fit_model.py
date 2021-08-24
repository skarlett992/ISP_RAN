def history_model(
        model, checkpoint_cb, earlystop_cb, class_weight,
        x_train_ptb, y_train_ptb, x_valid_ptb, y_valid_ptb
        ):

    history = model.fit(
        x_train_ptb, y_train_ptb,
        epochs=1, batch_size=32, steps_per_epoch = 10 ,
        validation_data=(x_valid_ptb, y_valid_ptb), validation_steps = 50,
        callbacks=[checkpoint_cb, earlystop_cb],
        verbose = 0,
        class_weight=class_weight)
    return history, model


