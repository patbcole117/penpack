# /usr/share/first-time-setup/first-time-setup.sh

ftsdir='/usr/share/first-time-setup/'

# ZSH
sudo apt install zsh
chsh -s $(which zsh)

# ZSH SYNTAX HILIGHTING
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ftsdir}zsh-syntax-hilighting
echo "source ${ftsdir}zsh-syntax-hilighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
source /usr/share/first-time-setup/zsh-syntax-hilighting/zsh-syntax-highlighting.zsh

# TMUX
https://github.com/tmux-plugins/tpm
https://github.com/tmux-plugins/tmux-resurrect
https://github.com/jimeh/tmux-themepack