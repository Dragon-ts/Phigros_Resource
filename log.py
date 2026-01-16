import logging
import sys
from typing import Optional


def init_console_logger(
        name: Optional[str] = None,
        level: int = logging.INFO,
        log_format: Optional[str] = None
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()
    if log_format is None:
        log_format = (
            "\033[36m%(asctime)s\033[0m "
            "\033[1;%(color)s%(levelname)-8s\033[0m " 
            "%(message)s"
        )
    level_colors = {
        logging.DEBUG: "37m",  # 白色
        logging.INFO: "32m",  # 绿色
        logging.WARNING: "33m",  # 黄色
        logging.ERROR: "31m",  # 红色
        logging.CRITICAL: "41m",  # 红底白字
    }

    class ColoredFormatter(logging.Formatter):
        def format(self, record):
            record.color = level_colors.get(record.levelno, "37m")
            return super().format(record)

    console_handler = logging.StreamHandler(sys.stdout)
    console_formatter = ColoredFormatter(
        log_format,
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    logger.propagate = False

    return logger


# ------------------------------
# 使用示例
# ------------------------------
if __name__ == "__main__":
    # 初始化仅控制台的Logger


    # 测试不同级别日志
    logger.debug("✅ 调试信息：加载 typetree.json 成功")
    logger.info("📌 普通信息：开始解析 APK 内 Unity 资源")
    logger.warning("⚠️ 警告信息：APK 内未找到 assets/aa/Android/level0 文件")
    logger.error("❌ 错误信息：解析 GameInformation 类型树失败")
    logger.critical("💥 严重错误：APK 文件损坏，无法读取")