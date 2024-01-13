import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_saved_model("models/ViT_on_10_epochs.model/")
tflite_model = converter.convert()
with open("models/converted_model.tflite", "wb") as f:
   f.write(tflite_model)