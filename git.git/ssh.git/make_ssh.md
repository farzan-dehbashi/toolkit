## To generate an ssh key:
```
ssh-keygen -t rsa -b 4096 -C 'email@email.com'
```
Then the key will be stored in /Users/<username>/.ssh/ directory.
There are two keys generated in that directore. <name>.pub which should be uploaded to github and is your public key and <name> file which is your private key.
Then you should make sure that you add the public key to the github account in settings tab. You should paste the text of the public key.
Later on you should make sure that the bash is able to use your private key when needed to inform github about your identity. To do so, see [this link](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
