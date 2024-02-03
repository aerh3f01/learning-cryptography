import hashlib
import itertools
import multiprocessing
from multiprocessing import Manager, Pool
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define Hash Type Detection
def identify_hash_type(hash_string):
    hash_length = len(hash_string)
    if hash_length == 32:
        print("MD5")
        return 'MD5'
    elif hash_length == 40:
        print("SHA-1")
        return 'SHA-1'
    elif hash_length == 64:
        print("SHA-256")
        return 'SHA-256'
    elif hash_length == 128:
        print("SHA-512")
        return 'SHA-512'
    else:
        return 'Unknown'

# Cracking Functions for Different Hash Types
def crack_md5(target_hash, charset, password_length, found_event):
    for item in itertools.product(charset, repeat=password_length):
        if found_event.is_set():
            break
        attempt = ''.join(item)
        hashed_attempt = hashlib.md5(attempt.encode()).hexdigest()
        print(f"Hash Type: MD5, Attempt: {attempt}, Hash: {hashed_attempt}")
        if hashed_attempt == target_hash:
            logging.info(f"Password found: {attempt}")
            found_event.set()
            return attempt
    return None

def crack_sha1(target_hash, charset, password_length, found_event):
    for item in itertools.product(charset, repeat=password_length):
        if found_event.is_set():
            break
        attempt = ''.join(item)
        hashed_attempt = hashlib.sha1(attempt.encode()).hexdigest()
        print(f"Hash Type: SHA-1, Attempt: {attempt}, Hash: {hashed_attempt}")
        if hashed_attempt == target_hash:
            logging.info(f"Password found: {attempt}")
            found_event.set()
            return attempt
    return None

def crack_sha256(target_hash, charset, password_length, found_event):
    for item in itertools.product(charset, repeat=password_length):
        if found_event.is_set():
            break
        attempt = ''.join(item)
        hashed_attempt = hashlib.sha256(attempt.encode()).hexdigest()
        print(f"Hash Type: SHA-256, Attempt: {attempt}, Hash: {hashed_attempt}")
        if hashed_attempt == target_hash:
            logging.info(f"Password found: {attempt}")
            found_event.set()
            return attempt
    return None


def crack_sha512(target_hash, charset, password_length, found_event):
    for item in itertools.product(charset, repeat=password_length):
        if found_event.is_set():
            break
        attempt = ''.join(item)
        hashed_attempt = hashlib.sha512(attempt.encode()).hexdigest()
        print(f"Hash Type: SHA-512, Attempt: {attempt}, Hash: {hashed_attempt}\n")
        if hashed_attempt == target_hash:
            logging.info(f"Password found: {attempt}")
            found_event.set()
            return attempt
    return None

# Distribute Cracking Based on Hash Type and Password Length
def distribute_cracking(target_hash, charset, min_length, max_length):
    hash_type = identify_hash_type(target_hash)
    cpu_count = multiprocessing.cpu_count()
    
    with Manager() as manager:
        found_event = manager.Event()
        
        with Pool(processes=cpu_count) as pool:
            if hash_type == 'MD5':
                crack_function = crack_md5
            elif hash_type == 'SHA-512':
                crack_function = crack_sha512
            elif hash_type == 'SHA-256':
                crack_function = crack_sha256
            elif hash_type == 'SHA-1':
                crack_function = crack_sha1
            else:
                logging.error(f"Hash type {hash_type} not supported.")
                return None

            tasks = []
            for length in range(min_length, max_length + 1):
                for char in charset:
                    tasks.append((target_hash, charset, length, found_event))

            try:
                async_result = pool.starmap_async(crack_function, tasks)
                results = async_result.get(timeout=10000)  # Adjust timeout as needed
            except KeyboardInterrupt:
                logging.info("Process interrupted by user.")
            except Exception as e:
                logging.error(f"Error occurred: {e}")
                pool.terminate()
            finally:
                pool.join()

            if results:
                for result in results:
                    if result:
                        return result

        logging.info("Password not found.")
        return None

# Main Function
def main():
    target_hash = "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043"  # Replace with the target hash, example should be SHA-512 - "hello"

    charset = "abcdefghijklmnopqrstuvwxyz"  # Extend or adapt as needed
    min_length = 5  # Minimum password length to start with
    max_length = 12 # Maximum password length to attempt

    logging.info("Starting password cracking...")
    found_password = distribute_cracking(target_hash, charset, min_length, max_length)
    if found_password:
        logging.info(f"Cracked password: {found_password}")
    else:
        logging.info("Failed to crack the password.")

if __name__ == "__main__":
    main()
