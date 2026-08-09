import os
import numpy as np
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam


# ============================================================
# SETTINGS
# ============================================================

TRAIN_DIR = r"algo code/dataset/train"
TEST_DIR = r"algo code/dataset/test"

IMG_SIZE = (64, 64)
BATCH_SIZE = 16
EPOCHS = 15


# ============================================================
# DATA
# ============================================================

datagen = ImageDataGenerator(rescale=1.0 / 255.0)

train_data = datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=True
)

test_data = datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)


print("\nCLASS MAPPING:")
print(train_data.class_indices)

print("\nTraining images:", train_data.samples)
print("Testing images:", test_data.samples)
print("Number of classes:", train_data.num_classes)


# ============================================================
# MODEL
# ============================================================

model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(64, 64, 3)),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),

    Conv2D(128, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),

    Flatten(),

    Dense(128, activation="relu"),
    Dropout(0.5),

    Dense(train_data.num_classes, activation="softmax")
])


model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


model.summary()


# ============================================================
# TRAIN
# ============================================================

history = model.fit(
    train_data,
    validation_data=test_data,
    epochs=EPOCHS
)


# ============================================================
# EVALUATE
# ============================================================

loss, accuracy = model.evaluate(test_data)

print("\n====================================")
print("TEST LOSS:", loss)
print("TEST ACCURACY:", accuracy)
print("====================================")


# ============================================================
# SAVE
# ============================================================

model.save("model_8class.h5")

print("\nMODEL SAVED AS: model_8class.h5")