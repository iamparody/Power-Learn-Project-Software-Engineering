# Ethical Analysis of AI Models

## MNIST Model Biases & Mitigation

### Potential Biases:
1. **Representation Bias**: MNIST contains only centered, white-on-black digits. Real-world digits may be skewed, colored, or noisy.
2. **Style Bias**: All digits are written in similar styles. Unusual handwriting may be misclassified.
3. **Cultural Bias**: Western/Arabic numeral focus only.

### Mitigation Strategies:
- **Data Augmentation**: Use TensorFlow's image augmentation (rotation, scaling, noise) to increase diversity
- **Transfer Learning**: Fine-tune on more diverse digit datasets
- **Fairness Indicators**: Use TensorFlow Fairness Indicators to check for performance across different writing styles

## Amazon Reviews Model Biases & Mitigation

### Potential Biases:
1. **Linguistic Bias**: Rule-based system can't understand sarcasm, context, or complex language.
2. **Vocabulary Bias**: Limited to pre-defined word lists. Misses emerging slang or domain-specific terms.
3. **Cultural Bias**: Sentiment words may have different meanings across cultures.
4. **Entity Recognition Bias**: spaCy's NER may favor well-known brands over smaller companies.

### Mitigation Strategies:
- **Use Trained Models**: Replace rule-based sentiment with BERT or other transformer models
- **Expand Vocabulary**: Continuously update word lists with real user feedback
- **Context Awareness**: Implement dependency parsing to understand negation ("not good")
- **Bias Testing**: Test model across diverse demographic groups and product categories

## General Ethical Principles Applied:
1. **Transparency**: Clear documentation of model limitations
2. **Fairness**: Regular bias audits and mitigation
3. **Privacy**: Anonymization of user review data
4. **Accountability**: Human oversight for high-stakes decisions



