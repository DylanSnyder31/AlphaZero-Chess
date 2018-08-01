# Machine-Learning-Chess
This is a Python implemenatation of Google Deepmind's AlpahZero. This project uses the GUI and chess engine based on my last [Repository](https://github.com/DylanSnyder31/GUI-Chess-Implementation-in-Python). 

## Getting Started

### Dependencies
```
pip install -r requirements.txt
```
#### Training 
To continue training model run:
```
python Train_Agent.py
```
To train the model from scratch in deep_structure.py comment out these lines:
```
75| if True:
76|    data_NN = torch.load(file, map_location=lambda storage, loc: storage)
77|    self.Neural_Network_Architecture.load_state_dict(data_NN)
```
#### Playing 
To play against the agent run:
```
python Play_Agent.py
```

## Resources 
#### Research Papers
[Mastering The Game of Go Without Human knowledge](https://www.nature.com/articles/nature24270.epdf?author_access_token=VJXbVjaSHxFoctQQ4p2k4tRgN0jAjWel9jnR3ZoTv0PVW4gB86EEpGqTRDtpIz-2rmo8-KG06gqVobU5NSCFeHILHcVFUeMsbvwS-lxjqQGg98faovwjxeTUgZAUMnRQ)  

[Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](https://arxiv.org/pdf/1712.01815.pdf)  
#### Articles
[AlphaGo Zero - How and Why it Works](http://tim.hibal.org/blog/alpha-zero-how-and-why-it-works/)  

[How to build your own AlphaZero AI using Python and Keras](https://medium.com/applied-data-science/how-to-build-your-own-alphazero-ai-using-python-and-keras-7f664945c188)  

[A Simple Alpha(Go) Zero Tutorial](https://web.stanford.edu/~surag/posts/alphazero.html)  

[General Game-Playing With Monte Carlo Tree Search](https://medium.com/@quasimik/monte-carlo-tree-search-applied-to-letterpress-34f41c86e238)  
#### Repositories
[suragnair/alpha-zero-general](https://github.com/suragnair/alpha-zero-general)  

[Zeta36/chess-alpha-zero](https://github.com/Zeta36/chess-alpha-zero)  
## Licence
MIT © Dylan Snyder
