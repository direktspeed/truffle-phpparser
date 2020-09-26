package org.trufflephp.runtime.array;

import org.trufflephp.runtime.PhpRuntime;

/**
 * @author abertschi
 */
public final class ArrayFactory {

    public static PhpArray newArray() {
        final int capacity = PhpRuntime.INITIAL_ARRAY_CAPACITY;
        return newArray(capacity);
    }

    public static PhpArray newArray(int capacity) {
        return new PhpArray(LongArrayAllocator.INSTANCE.createArray(capacity), capacity);
    }

    public static PhpArray newArray(Object backend, int cap) {
        return new PhpArray(backend, cap);
    }
}
