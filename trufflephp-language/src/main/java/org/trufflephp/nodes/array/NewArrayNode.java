package org.trufflephp.nodes.array;

import com.oracle.truffle.api.frame.VirtualFrame;
import org.trufflephp.nodes.PhpExprNode;
import org.trufflephp.runtime.array.ArrayFactory;
import org.trufflephp.runtime.array.PhpArray;

/**
 * Creates a new long based array node, which generalizes if needed.
 *
 * @author abertschi
 */
public final class NewArrayNode extends PhpExprNode {
    
    @Override
    public PhpArray executeGeneric(VirtualFrame frame) {
        return ArrayFactory.newArray();
    }
}
