# Negation And Speculation Detection from clinical text written in Spanish
The detection of speculation and negation in medical texts is paramount as otherwise extracted information can be incorrectly identified as real or factual events.
Speculation and negation detection is commonly divided into two sub-tasks: <strong>cue identification</strong> and <strong>scope recognition </strong>. Cues are words or terms that express negation (e.g, not, nothing, negative) or speculation (e.g., possible, probable, suggest). The scope is the text fragment affected by the corresponding cue in a sentence.<br><br>
This repository contains a deep learning-based approach for speculation and negation detection from clinical texts written in Spanish. The approach addresses negation and speculation detection as a sequence-labeling task, where each token in a sentence is classified as being part of the cue or the scope. This approach recognizes cues and scopes using the BIO tagging format.


This approach performs negation and speculation detection as a sequence labeling task. The proposed approach explores two deep learning methods: 
 <ul>

 <li> <strong>Bidirectional Long Short memory (BiLSTM): </strong>
 <li> <strong> Bidirectional Encoder Representation for Transformers (BERT): <strong>  
</ul>
