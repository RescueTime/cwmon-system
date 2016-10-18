=====
Usage
=====

Monitoring a Machine
====================

Once you've install ``cwmon-system``, using it is as simple as invoking
``cwmon system``. The following caveats apply:

#) Your AWS API credentials need to be available in a manner
   understandable by boto3_.

.. _boto3: http://boto3.readthedocs.io/en/latest/

To be truly useful, you probably need to automate this. The most
straightforward way to do this is probably via a crontab entry, e.g., ::

    3 * * * * cwmon system free_space free_inodes

.. note: This assumes that the cron job is running in a context where
         the above caveats are true. If not, then you would need to
         address that issue.
