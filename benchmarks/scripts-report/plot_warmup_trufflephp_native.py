from bench_db import get_timings_by_id
from bench_graphs import do_warmup_plot

num_iter = 7
color_copy_by_ref = 'green'
name = 'native-'


def warmup_all_plots():
    warmup_plot_fannkuch()
    warmup_plot_spectralnorm()
    warmup_plot_bintree()


def warmup_plot_fannkuch():
    ids = [
         100  # fannkuchredux-1, 2020-08-30 21:14, trufflephp-native
        , 102  # fannkuchredux-1, 2020-08-30 21:39, trufflephp-native
        , 104  # fannkuchredux-1, 2020-08-30 22:03, trufflephp-native
        , 106  # fannkuchredux-1, 2020-08-30 22:28, trufflephp-native
        , 108  # fannkuchredux-1, 2020-08-30 22:52, trufflephp-native
        , 110  # fannkuchredux-1, 2020-08-30 23:16, trufflephp-native
        , 112  # fannkuchredux-1, 2020-08-30 23:40, trufflephp-native
        , 114  # fannkuchredux-1, 2020-08-31 00:04, trufflephp-native
        , 116  # fannkuchredux-1, 2020-08-31 00:28, trufflephp-native
    ]
    runs = [get_timings_by_id(i, warmup=0) for i in ids]
    do_warmup_plot('fannkuchredux \ncopy-by-val', runs, num_iter=num_iter, subtitle='',
                   file_prefix=name)
    pass


def warmup_plot_spectralnorm():
    ids_by_val = [
         118  # spectralnorm-by-val,  2020-08-31 00:31:52, trufflephp-native
        , 122  # spectralnorm-by-val,  2020-08-31 00:37:51, trufflephp-native
        , 126  # spectralnorm-by-val,  2020-08-31 00:43:51, trufflephp-native
        , 130  # spectralnorm-by-val,  2020-08-31 00:49:50, trufflephp-native
        , 134  # spectralnorm-by-val,  2020-08-31 00:55:49, trufflephp-native
        , 138  # spectralnorm-by-val,  2020-08-31 01:01:48, trufflephp-native
        , 142  # spectralnorm-by-val,  2020-08-31 01:07:47, trufflephp-native
        , 146  # spectralnorm-by-val,  2020-08-31 01:13:47, trufflephp-native
        , 150  # spectralnorm-by-val,  2020-08-31 01:19:46, trufflephp-native
    ]

    runs = [get_timings_by_id(i, warmup=0) for i in ids_by_val]
    do_warmup_plot('spectralnorm \ncopy-by-val', runs, num_iter=num_iter,
                   file_prefix=name)

    ids_by_ref = [
        120  # spectralnorm-by-ref 2020-08-31 00:34:57, trufflephp-native
        , 124  # spectralnorm-by-ref 2020-08-31 00:40:56, trufflephp-native
        , 128  # spectralnorm-by-ref 2020-08-31 00:46:55, trufflephp-native
        , 132  # spectralnorm-by-ref 2020-08-31 00:52:54, trufflephp-native
        , 136  # spectralnorm-by-ref 2020-08-31 00:58:54, trufflephp-native
        , 140  # spectralnorm-by-ref 2020-08-31 01:04:53, trufflephp-native
        , 144  # spectralnorm-by-ref 2020-08-31 01:10:52, trufflephp-native
        , 148  # spectralnorm-by-ref 2020-08-31 01:16:51, trufflephp-native
        , 152  # spectralnorm-by-ref 2020-08-31 01:22:50, trufflephp-native
    ]

    runs = [get_timings_by_id(i, warmup=0) for i in ids_by_ref]
    do_warmup_plot('spectralnorm \ncopy-by-ref', runs, num_iter=num_iter,
                   color=color_copy_by_ref,
                   file_prefix=name)
    pass


def warmup_plot_bintree():
    ids_by_val = [
          156  # binary-trees-by-val, 2020-09-01 01:57:02, trufflephp-native
        , 160  # binary-trees-by-val, 2020-09-01 07:20:34, trufflephp-native
        , 164  # binary-trees-by-val, 2020-09-01 12:48:38, trufflephp-native
    ]

    runs = [get_timings_by_id(i, warmup=0) for i in ids_by_val]
    do_warmup_plot('binary-trees \ncopy-by-val', runs, num_iter=num_iter,
                   file_prefix=name)


    ids_by_ref = [
          169  # binary-trees-by-ref, 2020-09-01 14:40:30, trufflephp-native
        , 171  # binary-trees-by-ref, 2020-09-01 14:48:10, trufflephp-native
        , 173  # binary-trees-by-ref, 2020-09-01 14:55:38, trufflephp-native
        , 175  # binary-trees-by-ref, 2020-09-01 15:03:06, trufflephp-native
        , 177  # binary-trees-by-ref, 2020-09-01 15:10:40, trufflephp-native
        , 179  # binary-trees-by-ref, 2020-09-01 15:18:15, trufflephp-native
        , 181  # binary-trees-by-ref, 2020-09-01 15:25:48, trufflephp-native
        , 183  # binary-trees-by-ref, 2020-09-01 15:33:23, trufflephp-native
        , 185  # binary-trees-by-ref, 2020-09-01 15:40:56, trufflephp-native
    ]
    runs = [get_timings_by_id(i, warmup=0) for i in ids_by_ref]
    do_warmup_plot('binary-trees \ncopy-by-ref', runs, num_iter=num_iter,
                   color=color_copy_by_ref,
                   file_prefix=name)
    pass


if __name__ == '__main__':
    warmup_plot_fannkuch()
    warmup_plot_spectralnorm()
    warmup_plot_bintree()