from bench_db import get_timings_by_id
from bench_graphs import do_warmup_plot

num_iter = 7
color_copy_by_ref = 'green'


def warmup_all_plots():
    warmup_plot_fannkuch()
    warmup_plot_spectralnorm()
    # warmup_plot_bintree()


def warmup_plot_fannkuch():
    ids = [
        99  # 2020-08-30,  trufflephp   , fannkuchredux-1
        , 101  # 2020-08-30,  trufflephp, fannkuchredux-1
        , 103  # 2020-08-30,  trufflephp, fannkuchredux-1
        , 105  # 2020-08-30,  trufflephp, fannkuchredux-1
        , 107  # 2020-08-30,  trufflephp, fannkuchredux-1
        , 109  # 2020-08-30,  trufflephp, fannkuchredux-1
        , 111  # 2020-08-30,  trufflephp, fannkuchredux-1
        , 113  # 2020-08-31,  trufflephp, fannkuchredux-1
        , 115  # 2020-08-31,  trufflephp, fannkuchredux-1
    ]
    runs = [get_timings_by_id(i, warmup=0) for i in ids]
    do_warmup_plot('fannkuchredux \ncopy-by-val', runs, num_iter=num_iter, subtitle='',
                   file_prefix='trufflephp-')
    pass


def warmup_plot_spectralnorm():
    ids_by_val = [
        117  # spectralnorm-by-val, 2020-08-31 00:31,  trufflephp
        , 121  # spectralnorm-by-val, 2020-08-31 00:37,  trufflephp
        , 125  # spectralnorm-by-val, 2020-08-31 00:43,  trufflephp
        , 129  # spectralnorm-by-val, 2020-08-31 00:49,  trufflephp
        , 133  # spectralnorm-by-val, 2020-08-31 00:55,  trufflephp
        , 137  # spectralnorm-by-val, 2020-08-31 01:01,  trufflephp
        , 141  # spectralnorm-by-val, 2020-08-31 01:07,  trufflephp
        , 145  # spectralnorm-by-val, 2020-08-31 01:13,  trufflephp
        , 149  # spectralnorm-by-val, 2020-08-31 01:19,  trufflephp
    ]

    runs = [get_timings_by_id(i, warmup=0) for i in ids_by_val]
    do_warmup_plot('spectralnorm \ncopy-by-val', runs, num_iter=num_iter,
                   file_prefix='trufflephp-')

    ids_by_ref = [
        119  # spectralnorm-by-ref, 2020-08-31 00:34,  trufflephp
        , 123  # spectralnorm-by-ref, 2020-08-31 00:40,  trufflephp
        , 127  # spectralnorm-by-ref, 2020-08-31 00:46,  trufflephp
        , 131  # spectralnorm-by-ref, 2020-08-31 00:52,  trufflephp
        , 135  # spectralnorm-by-ref, 2020-08-31 00:58,  trufflephp
        , 139  # spectralnorm-by-ref, 2020-08-31 01:04,  trufflephp
        , 143  # spectralnorm-by-ref, 2020-08-31 01:10,  trufflephp
        , 147  # spectralnorm-by-ref, 2020-08-31 01:16,  trufflephp
        , 151  # spectralnorm-by-ref, 2020-08-31 01:22,  trufflephp
    ]

    runs = [get_timings_by_id(i, warmup=0) for i in ids_by_ref]
    do_warmup_plot('spectralnorm \ncopy-by-ref', runs, num_iter=num_iter,
                   color=color_copy_by_ref,
                   file_prefix='trufflephp-')
    pass


def warmup_plot_bintree():
    ids_by_val = [
          155  # binary-trees-by-val, 2020-09-01 01:57:02,  trufflephp
        , 159  # binary-trees-by-val, 2020-09-01 07:20:34,  trufflephp
        , 163  # binary-trees-by-val, 2020-09-01 12:48:38,  trufflephp
    ]

    runs = [get_timings_by_id(i, warmup=0) for i in ids_by_val]
    do_warmup_plot('binary-trees \ncopy-by-val', runs, num_iter=num_iter,
                   file_prefix='trufflephp-')

    ids_by_ref = [
          168  # binary-trees-by-ref, 2020-09-01 14:40:30, trufflephp
        , 170  # binary-trees-by-ref, 2020-09-01 14:48:10, trufflephp
        , 172  # binary-trees-by-ref, 2020-09-01 14:55:38, trufflephp
        , 174  # binary-trees-by-ref, 2020-09-01 15:03:06, trufflephp
        , 176  # binary-trees-by-ref, 2020-09-01 15:10:40, trufflephp
        , 178  # binary-trees-by-ref, 2020-09-01 15:18:15, trufflephp
        , 180  # binary-trees-by-ref, 2020-09-01 15:25:48, trufflephp
        , 182  # binary-trees-by-ref, 2020-09-01 15:33:23, trufflephp
        , 184  # binary-trees-by-ref, 2020-09-01 15:40:56, trufflephp
    ]
    runs = [get_timings_by_id(i, warmup=0) for i in ids_by_ref]
    do_warmup_plot('binary-trees \ncopy-by-ref', runs, num_iter=num_iter,
                   color=color_copy_by_ref,
                   file_prefix='trufflephp-')
    pass


if __name__ == '__main__':
    warmup_plot_bintree()
    warmup_plot_fannkuch()
    warmup_plot_spectralnorm()