# -*- encoding: utf-8 -*-
"""Tests for the various metrics reported by the monitoring CLI."""
from unittest import mock
import pytest

from cwmon_system import metrics


def test_disk_metric_happy_path():
    """Create a :class:`DiskFreeSpaceMetric` and hope the root device has a reasonable amount of free space."""
    m = metrics.DiskFreeSpaceMetric("/")
    assert "GiB" == m.unit


def test_disk_percent_metric_happy_path():
    """Create a :class:`DiskPercentFreeSpaceMetric` and hope the root device has a reasonable amount of free space."""
    m = metrics.DiskPercentFreeSpaceMetric("/")
    assert m.value > 5


def test_inode_metric_happy_path():
    """Create a :class:`DiskFreeInodesMetric` and hope the root device has a reasonable number of free inodes."""
    m = metrics.DiskFreeInodesMetric("/")
    assert m.value > 10000


def test_inode_percent_metric_happy_path():
    """Create a :class:`DiskPercentFreeInodesMetric` and hope the root device has a reasonable number of free inodes."""
    m = metrics.DiskPercentFreeInodesMetric("/")
    assert m.value > 5


def test_total_process_metric_happy_path():
    """Create a :class:`TotalProcessesMetric` and hope the machine is running at a somewhat normal load.

    .. note:: "Normal" is based on whatever load happened to be active on the dev machine when the test was written.
    """
    m = metrics.TotalProcessesMetric()
    assert 1 < m.value < 600  # This is a guess.


def test_zombie_process_metric_happy_path():
    """Create a :class:`ZombieProcessesMetric` and hope the machine is running at a somewhat normal load.

    .. note:: "Normal" is based on whatever load happened to be active on the dev machine when the test was written.
    """
    m = metrics.ZombieProcessesMetric()
    assert 0 <= m.value < 25  # This is a guess.


def test_1min_load_avg_metric_happy_path():
    """Create a :class:`OneMinuteLoadAvgMetric` and hope we don't get an error."""
    m = metrics.OneMinuteLoadAvgMetric()
    assert 0 < m.value < 100


def test_5min_load_avg_metric_happy_path():
    """Create a :class:`FiveMinuteLoadAvgMetric` and hope we don't get an error."""
    m = metrics.OneMinuteLoadAvgMetric()
    assert 0 < m.value < 100


def test_15min_load_avg_metric_happy_path():
    """Create a :class:`FifteenMinuteLoadAvgMetric` and hope we don't get an error."""
    m = metrics.OneMinuteLoadAvgMetric()
    assert 0 < m.value < 100


def test_cpu_percentage_metric_happy_path():
    """Create a :class:`CpuPercentageMetric` and hope we don't get an error."""
    m = metrics.CpuPercentageMetric()
    assert 0 < m.value < 100


def test_cpu_context_switch_metric_happy_path():
    """Create a :class:`CpuContextSwitchesMetric` and hope we don't get an error."""
    m = metrics.CpuContextSwitchesMetric()
    assert m.value > 0


def test_memory_available_metric_happy_path():
    """Create a :class:`MemoryAvailableMetric` and hope we don't get an error."""
    m = metrics.MemoryAvailableMetric()
    assert m.value > 0
    assert m.unit is not None


def test_memory_available_percentage_metric_happy_path():
    """Create a :class:`MemoryAvailablePercentageMetric` and hope we don't get an error."""
    m = metrics.MemoryAvailablePercentageMetric()
    assert m.value > 0
