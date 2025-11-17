## Common TensorFlow Debugging Solutions

### Error 1: Dimension Mismatch in CNN
**Problem**: `Input 0 of layer "conv2d" is incompatible with the layer`
**Solution**: 
x_train = x_train.reshape(-1, 28, 28, 1)  # Add channel dimension

# For multi-class (10 digits)
model.compile(loss='categorical_crossentropy', ...)
# Or for integer labels
model.compile(loss='sparse_categorical_crossentropy', ...)

# Add regularization
model.add(layers.Dropout(0.5))
model.add(layers.BatchNormalization())
# Use early stopping
early_stopping = tf.keras.callbacks.EarlyStopping(patience=3)


### **Day 3 Success Checklist:**
- [ ] spaCy NER successfully extracts brands and products
- [ ] Rule-based sentiment provides reasonable results
- [ ] Clear visualizations of sentiment and entity distribution
- [ ] Comprehensive ethics analysis completed
- [ ] All screenshots taken for final report

