## pyclone
A small script to download all of the **public** repos of a user.

## Requirements

1. git
2. python
3. BeautifulSoup package
4. requests package

Before using, be sure that you have installed `git`, `python`, `requests` and `BeautifulSoup` packages. In order to install required packages, you can run `pip install -r requirements.txt`.

## Usage

`pyclone`  
    If you don't pass any parameter, you will be prompted for `username` and `destination folder`.
  

  or


`pyclone <username>`  
    If you don't pass any location folder parameter, by default repos will be cloned into current folder `.`.


  or

  
`pyclone <username> <destination-folder>`  
    Repos from `username` will be cloned into the folder that you passed.