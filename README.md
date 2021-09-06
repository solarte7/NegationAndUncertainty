# NegationAndSpeculation
The detection of speculation and negation in medical texts is paramount as otherwise extracted information can be incorrectly identified as real or factual events.
Speculation and negation detection is commonly divided into two sub-tasks: <strong>cue identification and scope recognition </strong>. Cues are words or terms that express negation (e.g, not, nothing, negative) or speculation (e.g., possible, probable, suggest). The scope is the text fragment affected by the corresponding cue in a sentence.<br>
This repository contains a deep learning-based approach for speculation and negation detection from clinical texts written in Spanish. This approach performs negation and speculation detection as a sequence labeling task. The proposed approach explores two deep learning methods: 
 <ul>

 <li> Bidirectional Long Short memory (BiLSTM)
 <li> Bidirectional Encoder Representation for Transformers (BERT)  
</ul>
