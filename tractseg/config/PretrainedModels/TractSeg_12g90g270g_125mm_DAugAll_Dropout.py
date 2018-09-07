import os
from tractseg.config.TractSegHP import HP as TractSegHP


class HP(TractSegHP):
    EXP_NAME = os.path.basename(__file__).split(".")[0]

    NUM_EPOCHS = 500
    DATA_AUGMENTATION = True
    USE_DROPOUT = True