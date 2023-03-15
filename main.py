from rgb import rgb_clustering
from hsv import hsv_clustering
from hsv2 import hsv2_clustering

# image_name = input('Image name: ')
# image_path = f'test/{image_name}'
# mode = input('Color model: ')
# count_clusters = int(input('Count of clusters: '))

# if mode == 'rgb' or mode == '1':
#     rgb_clustering(image_path, count_clusters)
# elif mode == 'hsv' or mode == '2':
#     hsv_clustering(image_path, count_clusters)
# elif mode == 'all' or mode == '3':
#     rgb_clustering(image_path, count_clusters)
#     hsv_clustering(image_path, count_clusters)

rgb_clustering('images/00000003_(7).jpg', 8)

'''
                              __gggrgM**M#mggg__
                          __wgNN@"B*P""mp""@d#"@N#Nw__
                        _g#@0F_a*F#  _*F9m_ ,F9*__9NG#g_
                     _mN#F  aM"    #p"    !q@    9NL "9#Qu_
                    g#MF _pP"L  _g@"9L_  _g""#__  g"9w_ 0N#p
                  _0F jL*"   7_wF     #_gF     9gjF   "bJ  9h_
                 j#  gAF    _@NL     _g@#_      J@u_    2#_  #_
                ,FF_#" 9_ _#"  "b_  g@   "hg  _#"  !q_ jF "*_09_
░█████╗░░█████╗░██╗░░░░░░█████╗░██████╗░░██████╗███████╗███╗░░██╗░██████╗███████╗
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░██║██╔════╝██╔════╝
██║░░╚═╝██║░░██║██║░░░░░██║░░██║██████╔╝╚█████╗░█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░██╗██║░░██║██║░░░░░██║░░██║██╔══██╗░╚═══██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
╚█████╔╝╚█████╔╝███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░╚███║██████╔╝███████╗
░╚════╝░░╚════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝
    █▄▄ █▄█   █░█ ▄▀█ █░░ █▀▀ █▀█ ▄▀█   █▀▄ █░█ ▄▀█   █▀ ▄▀█ █▀█ ▄▀█ █▄█ ▄▀█
    █▄█ ░█░   ▀▄▀ █▀█ █▄▄ ██▄ █▀▄ █▀█   █▄▀ ▀▄▀ █▀█   ▄█ █▀█ █▀▄ █▀█ ░█░ █▀█
                 9# "b_j   "b_ g"    *g _gF    9_ g#"  "L_*"qNF
                  "b_ "#_    "NL      _B#      _I@     j#" _#"
                    NM_0"*g_ j""9u_  gP  q_  _w@ ]_ _g*"F_g@
                     "NNh_ !w#_   9#g"    "m*"   _#*" _dN@"
                        9##g_0@q__ #"4_  j*"k __*NF_g#@P"
                          "9NN#gIPNL_ "b@" _2M"Lg#N@F"
                              ""P@*NN#gEZgNN@#@P""
'''