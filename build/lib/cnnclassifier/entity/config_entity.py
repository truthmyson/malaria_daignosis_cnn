# this will define the return type of  configurations
from pathlib import Path
from dataclasses import dataclass

# the class decorator allow us to add more functions to the class(like, frozen=true, makes the class variables immutable)
@dataclass(frozen=True) 
class DataIngestionConfig:
    """
    Data ingestion configurations and params return types
    Args:
        root_dir: Root directory for data ingestion
        dataset_path: Path to the dataset
        dataset_info_path: Path to dataset info file
        shuffle: Whether to shuffle the data
        with_info: Whether to include dataset info
        dataset_name: Name of the dataset
        as_supervised: Whether to load as supervised (features, labels)
        split: List of dataset splits to load
    """
    root_dir: Path
    dataset_path: Path
    dataset_info_path: Path 
    shuffle: bool
    with_info: bool
    dataset_name: str
    as_supervised: bool
    split: list[str]

# the class decorator allow us to add more functions to the class(like, frozen=true, makes the class variables immutable)
@dataclass(frozen=True)
class SplitDatasets:
    """
    split dataset cofiguration and params return types
    Args:
        root_dir: Root directory containing the splitted datasets
        train_path: Path to training dataset
        test_path: Path to testing dataset  
        validation_path: Path to validation dataset
        train_size: Proportion of data for training (0.0 to 1.0)
        test_size: Proportion of data for testing (0.0 to 1.0)
        validation_size: Proportion of data for validation (0.0 to 1.0)
    """
    root_dir: Path
    train_path: Path
    test_path: Path
    validation_path: Path
    dataset_path: Path
    train_size: float
    test_size: float
    validation_size: float

@dataclass(frozen=True)
class Preprocessing:
    """
    Preprocessing configuration and params
    Args:
        shuffe_size: size of data to be shuffled at a time
        batch_size: number of batches to divide the total dataaet into
        img_shape: the new shape of the image
    """
    shuffle_size: int
    batch_size: int
    img_shape: int

@dataclass(frozen=True)
class BUildModel:
    """
    model building configuration and params
    Args:
        train_path(Path): path to the training data
        validation_path(path): path to the validtion data
        model_path(Path): path to the model
    """
    train_path: Path
    validation_path: Path
    model_path: Path