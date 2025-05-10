
import logging,os,sys
from engine.scraper import GreyhoundScraper

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join("logs", "scraper.log")),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Greyhound Scraper")
if __name__ == "__main__":
    try:
        with GreyhoundScraper(headless=True, max_threads=130) as scraper:
            scraper.run()
    except KeyboardInterrupt:
        logger.info("Scraper stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)